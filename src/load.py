import ast
import logging
import click
from loader import SupermarketLoader
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@click.command()
@click.option('--file_paths', type=str, help="""
file paths in dictionary format with the information in csv format to load to the database \
example:\n
{\n
    'table_name_1':'/home/data/table_name_1.csv',\n
    'table_name_2':'/home/data/table_name_2.csv',\n
    ...\n
}\n

""")
def run(file_paths: str):
    """
   ETL process to save the price through the products time of the main supermarkets of Costa Rica. ඞ
      --------------------------------------------------------------------------------------------------
    Loads the transformed data from the selected supermarket to the dabase
    """
    logger.info('Starting the loading')
    file_paths = ast.literal_eval(file_paths)
    SupermarketLoader(file_paths).load()
    logger.info('Loading process done')
    logger.info('ETL process done')


if __name__ == '__main__':
    run()
