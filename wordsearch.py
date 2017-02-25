import os
import click

@click.command()
@click.argument('path', type=click.Path(exists=True))
def main(path):
    click.echo(os.path.abspath(path))
    