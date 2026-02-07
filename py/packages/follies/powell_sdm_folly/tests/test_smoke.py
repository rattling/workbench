"""Smoke test for Powell SDM folly"""

import subprocess
from pathlib import Path


def test_policy_a_runs():
    """Verify Policy A runs without error and produces output."""
    # Run for small T to keep test fast
    result = subprocess.run(
        [
            "python",
            "-m",
            "powell_sdm_folly.main",
            "--policy",
            "a",
            "--seed",
            "42",
            "--T",
            "5",
        ],
        cwd=Path(__file__).parent.parent.parent.parent,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, f"Policy A failed: {result.stderr}"

    # Check output file exists (runs dir is at py/packages/follies/runs/)
    runs_dir = Path(__file__).parent.parent.parent.parent / "follies" / "runs"
    trace_file = runs_dir / "policy_a_latest.txt"
    assert trace_file.exists(), f"Trace file not created at {trace_file}"


def test_policy_b_runs():
    """Verify Policy B runs without error and produces output."""
    result = subprocess.run(
        [
            "python",
            "-m",
            "powell_sdm_folly.main",
            "--policy",
            "b",
            "--seed",
            "42",
            "--T",
            "5",
        ],
        cwd=Path(__file__).parent.parent.parent.parent,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, f"Policy B failed: {result.stderr}"

    # Check output file exists (runs dir is at py/packages/follies/runs/)
    runs_dir = Path(__file__).parent.parent.parent.parent / "follies" / "runs"
    trace_file = runs_dir / "policy_b_latest.txt"
    assert trace_file.exists(), f"Trace file not created at {trace_file}"
