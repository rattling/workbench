"""
Trace comparison utility

Reads trace files from both policies and produces side-by-side comparison.
"""

from pathlib import Path


def compare_traces(
    trace_a: Path,
    trace_b: Path,
    n_steps: int = 10,
):
    """
    Compare two trace files side by side.

    Args:
        trace_a: Path to Policy A trace
        trace_b: Path to Policy B trace
        n_steps: Number of steps to show (default: first 10)
    """
    if not trace_a.exists():
        print(f"ERROR: {trace_a} not found")
        print("Run: python -m powell_sdm_folly.main --policy a --seed 42")
        return

    if not trace_b.exists():
        print(f"ERROR: {trace_b} not found")
        print("Run: python -m powell_sdm_folly.main --policy b --seed 42")
        return

    print("\n" + "=" * 80)
    print("TRACE COMPARISON: Policy A vs Policy B")
    print("=" * 80 + "\n")

    # Read both files
    with open(trace_a) as f:
        lines_a = f.readlines()

    with open(trace_b) as f:
        lines_b = f.readlines()

    # Show first n_steps (skip header lines)
    print(f"First {n_steps} steps:\n")
    print("Policy A (constant base-stock):")
    print("".join(lines_a[:2]))  # Header
    for line in lines_a[2 : 2 + n_steps]:
        print(line.rstrip())

    print("\n" + "-" * 80 + "\n")

    print("Policy B (forecast-driven with learning):")
    print("".join(lines_b[:2]))  # Header
    for line in lines_b[2 : 2 + n_steps]:
        print(line.rstrip())

    # Extract and show summaries
    print("\n" + "=" * 80)
    print("SUMMARY COMPARISON")
    print("=" * 80 + "\n")

    def extract_summary(lines):
        """Extract summary stats from trace file."""
        summary = {}
        for line in lines:
            if line.startswith("Total cost:"):
                summary["cost"] = float(line.split(":")[1].strip())
            elif line.startswith("Total stockouts:"):
                summary["stockouts"] = float(line.split(":")[1].strip())
            elif line.startswith("Average inventory:"):
                summary["inventory"] = float(line.split(":")[1].strip())
        return summary

    summary_a = extract_summary(lines_a)
    summary_b = extract_summary(lines_b)

    if summary_a and summary_b:
        print(f"{'Metric':<25} {'Policy A':>15} {'Policy B':>15} {'Difference':>15}")
        print("-" * 75)

        cost_diff = summary_b["cost"] - summary_a["cost"]
        cost_pct = (cost_diff / summary_a["cost"]) * 100 if summary_a["cost"] > 0 else 0
        print(
            f"{'Total Cost':<25} {summary_a['cost']:>15.2f} {summary_b['cost']:>15.2f} "
            f"{cost_diff:>15.2f} ({cost_pct:+.1f}%)"
        )

        so_diff = summary_b["stockouts"] - summary_a["stockouts"]
        print(
            f"{'Total Stockouts':<25} {summary_a['stockouts']:>15.2f} "
            f"{summary_b['stockouts']:>15.2f} {so_diff:>15.2f}"
        )

        inv_diff = summary_b["inventory"] - summary_a["inventory"]
        print(
            f"{'Average Inventory':<25} {summary_a['inventory']:>15.2f} "
            f"{summary_b['inventory']:>15.2f} {inv_diff:>15.2f}"
        )

    print("\n")


def main():
    """CLI entry point for comparison."""
    runs_dir = Path(__file__).parent.parent.parent.parent / "runs"
    trace_a = runs_dir / "policy_a_latest.txt"
    trace_b = runs_dir / "policy_b_latest.txt"

    compare_traces(trace_a, trace_b, n_steps=10)


if __name__ == "__main__":
    main()
