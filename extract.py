import click

@click.command()
@click.option('--supermarket', type=click.Choice([name for name in supermarkets.keys()]), help='The supermarket used in the ETL process')
def run():
    pass

if __name__ == '__main__':
    run()
