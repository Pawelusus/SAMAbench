"""Plot results"""

from pathlib import Path
from typing import Annotated, Literal

import typer


def plot_command(
    input_dirs: Annotated[
        list[Path], typer.Argument(help="Directories with data to plot.")
    ],
    backend: Annotated[
        Literal["native", "cocopp"], typer.Option(help="Plotter backend.")
    ] = "native",
) -> None:
    """Plots native plots or comparison via cocopp (olny for BBOB)."""
    raise NotImplementedError
