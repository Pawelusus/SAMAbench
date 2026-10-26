"""Experiment comparison"""

from pathlib import Path
from typing import Annotated

import typer


def compare_command(
    input_dirs: Annotated[
        list[Path], typer.Argument(help="Directories, containing results, to compare.")
    ],
    metric: Annotated[
        str, typer.Option(help="Metric to compare by from summary.json.")
    ] = "best_y",
) -> None:
    """Reads summary.json from each folder and prints comparison."""
    raise NotImplementedError
