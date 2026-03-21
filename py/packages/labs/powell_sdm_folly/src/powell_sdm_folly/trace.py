"""
Trace writer

Produces human-readable step-by-step logs of the SDM loop.
Primary learning artifact for understanding Powell's framework.
"""

from pathlib import Path
from powell_sdm_folly.env_inventory import StepRecord


class TraceWriter:
    """
    Writes fixed-format trace files.

    Each line records one complete time step through Powell's loop.
    Format is designed for human readability and side-by-side comparison.
    """

    def __init__(self, filepath: Path):
        """
        Initialize trace writer.

        Args:
            filepath: Output file path
        """
        self.filepath = filepath
        self.filepath.parent.mkdir(parents=True, exist_ok=True)
        self.file = None

    def __enter__(self):
        """Open file and write header."""
        self.file = open(self.filepath, "w")
        self._write_header()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close file."""
        if self.file:
            self.file.close()

    def _write_header(self):
        """Write column headers."""
        headers = [
            "t",
            "I_t",
            "q_t",
            "I_post",
            "D_t+1",
            "sales",
            "I_t+1",
            "stockout",
            "cost",
            "yhat",
            "err",
        ]
        self.file.write("  ".join(f"{h:>8}" for h in headers) + "\n")
        self.file.write("-" * (10 * len(headers) + len(headers) - 1) + "\n")

    def write_step(
        self,
        record: StepRecord,
        forecast: float | None = None,
        forecast_error: float | None = None,
    ):
        """
        Write one step to trace file.

        Args:
            record: Step record from environment
            forecast: Optional forecast (Policy B only)
            forecast_error: Optional forecast error (Policy B only)
        """
        values = [
            record.t,
            record.inventory_pre,
            record.order_qty,
            record.inventory_post,
            record.demand,
            record.sales,
            record.inventory_next,
            record.stockout,
            record.cost,
            forecast if forecast is not None else 0.0,
            forecast_error if forecast_error is not None else 0.0,
        ]

        # Format numeric values
        formatted = []
        for v in values:
            if isinstance(v, int) or (isinstance(v, float) and v == int(v)):
                formatted.append(f"{int(v):>8}")
            else:
                formatted.append(f"{v:>8.2f}")

        self.file.write("  ".join(formatted) + "\n")
        self.file.flush()  # Ensure immediate write


def write_summary(filepath: Path, records: list[StepRecord], policy_name: str):
    """
    Append summary statistics to trace file.

    Args:
        filepath: Trace file path
        records: List of step records
        policy_name: Name of policy for display
    """
    total_cost = sum(r.cost for r in records)
    total_stockouts = sum(r.stockout for r in records)
    avg_inventory = sum(r.inventory_next for r in records) / len(records)

    with open(filepath, "a") as f:
        f.write("\n")
        f.write("=" * 80 + "\n")
        f.write(f"Policy: {policy_name}\n")
        f.write(f"Total cost: {total_cost:.2f}\n")
        f.write(f"Total stockouts: {total_stockouts:.2f}\n")
        f.write(f"Average inventory: {avg_inventory:.2f}\n")
        f.write("=" * 80 + "\n")
