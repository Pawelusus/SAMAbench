"""Run experiment"""

from pathlib import Path
from typing import Annotated

import typer


def run_command(
    config_path: Annotated[
        Path,
        typer.Argument(
            exists=True, dir_okay=False, help="Experiment configuration (JSON)."
        ),
    ],
) -> None:
    """Runs experiment for every seed in config file."""
    raise NotImplementedError
