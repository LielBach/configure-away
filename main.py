import click


@click.command(name="configure-away")
@click.option("--path", required=False, type=str, default=".")
def main(path):
    pass


if __name__ == "__main__":
    main()
