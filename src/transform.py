import ast
import logging
import click
from transformer import TransformSupermarket
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@click.command()
@click.option('--args', type=str, help="""
args in dictionary format with the file path and the name of the supermarket \
example:\n
{\n
    'file_path':'/home/data/data.csv',\n
    'name':'pequeno_mundo'\n
}\n

""")
def run(args: str):
    """
    ETL process to save the price through the products time of the main supermarkets of Costa Rica. ඞ
   --------------------------------------------------------------------------------------------------
    Transforms the raw data from the selected supermarket

    """
    logger.info("Starting Transformation Process")
    args = ast.literal_eval(args)
    file_paths = TransformSupermarket(
        args['file_path'], args['name']).transform()

    # logger.info('Transformation process done')
    print(file_paths)


if __name__ == '__main__':
    run()
