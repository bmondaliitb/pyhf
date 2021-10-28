"""The pyhf Command Line Interface."""
import logging

import click
import typer

from pyhf import __version__
from pyhf.cli import rootio, spec, infer, patchset, complete
from pyhf.contrib import cli as contrib
from pyhf import utils

logging.basicConfig()
log = logging.getLogger(__name__)

app = typer.Typer()


@app.command()
def top():
    """
    Top level command, form Typer
    """
    typer.echo("The Typer app is at the top level")


@app.callback()
def callback():
    """
    Typer app, including Click subapp
    """


def _print_citation(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(utils.citation())
    ctx.exit()


@click.group(context_settings=dict(help_option_names=['-h', '--help']))
@click.version_option(version=__version__)
@click.option(
    "--cite",
    "--citation",
    help="Print the bibtex citation for this software",
    default=False,
    is_flag=True,
    callback=_print_citation,
    expose_value=False,
    is_eager=True,
)
def pyhf():
    """Top-level CLI entrypoint."""


typer_click_object = typer.main.get_command(app)

typer_click_object.add_command(pyhf)

# typer_click_object.add_command(rootio.cli)
typer_click_object.add_command(rootio.json2xml)
typer_click_object.add_command(rootio.xml2json)

# typer_click_object.add_command(spec.cli)
typer_click_object.add_command(spec.inspect)
typer_click_object.add_command(spec.prune)
typer_click_object.add_command(spec.rename)
typer_click_object.add_command(spec.combine)
typer_click_object.add_command(spec.digest)
typer_click_object.add_command(spec.sort)

# typer_click_object.add_command(infer.cli)
typer_click_object.add_command(infer.fit)
typer_click_object.add_command(infer.cls)

typer_click_object.add_command(patchset.cli)

typer_click_object.add_command(complete.cli)

typer_click_object.add_command(contrib.cli)
