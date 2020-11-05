import click

from intools.main import pass_context
from intools import __version__

@click.command()
@pass_context
def command(ctx, **kwargs):
    """Show version of InTools."""
    click.echo(f"Version: {__version__}")