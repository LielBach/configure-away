import click

from configuration_builder import build_configuration
from schema_discovery import discover_schema


@click.command(name="configure-away")
@click.option("--path", required=False, type=str, default=".")
def main(path):
    schema = discover_schema(path)
    build_configuration(schema)


if __name__ == "__main__":
    main()
