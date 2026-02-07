"""
Main entry point for Powell SDM Folly

Runs one policy through T time steps and writes trace file.
"""

import argparse
from pathlib import Path

from powell_sdm_folly.demand_process import generate_demands
from powell_sdm_folly.env_inventory import InventoryEnv
from powell_sdm_folly.policies import PolicyA, PolicyB
from powell_sdm_folly.trace import TraceWriter, write_summary


def run_policy(
    policy,
    demands: list[float],
    initial_inventory: float,
    output_path: Path,
    policy_name: str,
):
    """
    Run one policy through the SDM loop.

    Args:
        policy: Policy instance (A or B)
        demands: Pregenerated demand sequence
        initial_inventory: Starting inventory level
        output_path: Where to write trace file
        policy_name: Display name for policy
    """
    env = InventoryEnv(initial_inventory=initial_inventory)
    records = []

    print(f"\n{'='*60}")
    print(f"Running {policy_name}")
    print(f"{'='*60}\n")

    with TraceWriter(output_path) as trace:
        for t, demand in enumerate(demands):
            # Pre-decision state
            inventory = env.inventory

            # Decision (possibly using forecast)
            order_qty = policy.decide(inventory, t)

            # Get forecast info before stepping (for tracing)
            forecast = policy.get_forecast(t)

            # Step environment (post-decision → exogenous → transition)
            record = env.step(order_qty, demand)

            # Learning (update model after observing demand)
            policy.learn(t, demand)

            # Get forecast error (for tracing)
            forecast_error = policy.get_forecast_error(t, demand)

            # Write trace
            trace.write_step(record, forecast, forecast_error)
            records.append(record)

            # Progress indicator
            if (t + 1) % 7 == 0:
                print(f"Completed week {(t + 1) // 7}")

    # Write summary
    write_summary(output_path, records, policy_name)

    # Print results
    total_cost = sum(r.cost for r in records)
    total_stockouts = sum(r.stockout for r in records)
    avg_inventory = sum(r.inventory_next for r in records) / len(records)

    print(f"\nResults:")
    print(f"  Total cost: {total_cost:.2f}")
    print(f"  Total stockouts: {total_stockouts:.2f}")
    print(f"  Average inventory: {avg_inventory:.2f}")
    print(f"\nTrace written to: {output_path}")


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Run Powell SDM folly with specified policy"
    )
    parser.add_argument(
        "--policy",
        choices=["a", "b"],
        required=True,
        help="Policy to run: a (constant) or b (forecast-driven)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for demand generation (default: 42)",
    )
    parser.add_argument(
        "--T",
        type=int,
        default=56,
        help="Number of time periods to simulate (default: 84)",
    )

    args = parser.parse_args()

    # Generate demand sequence (same for all policies when using same seed)
    print(f"\nGenerating {args.T} periods of demand (seed={args.seed})...")
    demands = generate_demands(args.T, args.seed)

    # Setup output directory
    runs_dir = Path(__file__).parent.parent.parent.parent / "runs"
    runs_dir.mkdir(exist_ok=True)

    # Default parameters (pedagogical, not optimal)
    initial_inventory = 80.0

    # Run selected policy
    if args.policy == "a":
        policy = PolicyA(target_stock=90.0)
        output_path = runs_dir / "policy_a_latest.txt"
        policy_name = "Policy A (Constant Base-Stock)"
    else:
        policy = PolicyB(safety_stock=10.0, learning_rate=0.05)
        output_path = runs_dir / "policy_b_latest.txt"
        policy_name = "Policy B (Forecast-Driven with Learning)"

    run_policy(policy, demands, initial_inventory, output_path, policy_name)

    print(f"\n{'='*60}")
    print("Next steps:")
    if args.policy == "a":
        print("  Run Policy B: python -m powell_sdm_folly.main --policy b --seed 42")
    else:
        print("  Run Policy A: python -m powell_sdm_folly.main --policy a --seed 42")
    print("  Compare both: python -m powell_sdm_folly.compare")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
