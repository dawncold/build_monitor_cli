import click
from build_monitor_cli.main import main


@click.command()
@click.option('--org', required=True, help='organization alias in config file')
def entry(org):
    main(org)

if __name__ == '__main__':
    entry()
