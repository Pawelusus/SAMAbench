"""Status report of experiment (ongoing or done)"""

from pathlib import Path
from typing import Annotated

import typer


def status_command(
    input_dir: Annotated[
        Path, typer.Argument(exists=True, file_okay=False, help="Output directory.")
    ],
    watch: Annotated[bool, typer.Option(help="Refresh every few seconds.")] = False,
) -> None:
    """Prints newest checkpoint (iteration, best value, time)."""
    raise NotImplementedError
