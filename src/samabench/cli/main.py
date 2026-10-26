"""CLI entrypoint"""

import typer

from samabench.cli.compare import compare_command
from samabench.cli.plot import plot_command
from samabench.cli.run import run_command
from samabench.cli.status import status_command

app = typer.Typer(
    name="samabench",
    help="Surrogate Assisted Metaheurisctic Algorithms Benchmark.",
    no_args_is_help=True,
)

app.command("run")(run_command)
app.command("plot")(plot_command)
app.command("compare")(compare_command)
app.command("status")(status_command)
