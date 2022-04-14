from psycopg2 import IntegrityError
from sqlalchemy import create_engine, false
from load import SupermarketLoader
from spiders.pricesmart_spider import PriceSmartSpider
from spiders.pequeno_mundo_spider import PequenoMundoSpider
from supermarket import Supermarket
from scrapy.crawler import CrawlerProcess
import logging
import click
import os
from cfg import DATA_DIR
from transform import TransformSupermarket

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


supermarkets = {
    'pequeno_mundo': Supermarket(name='pequeno_mundo', spider=PequenoMundoSpider),
    'pricesmart': Supermarket(name='pricesmart', spider=PriceSmartSpider)
}


def _extract(supermarket: Supermarket) -> None:
    """ Start the CrawlerProcess to scrape the supermarket and extract the raw information.
    Args:
        supermarket (Supermarket): a Supermarket instance with the spider to scrape.
    """
    logger.info('Starting extraction process')
    # Delete csv if exists
    try:
        os.remove(supermarket.file_path)
        logger.info(f'File in {supermarket.file_path} removed')
    except FileNotFoundError as err:
        logger.info(f'File in {supermarket.file_path} does not exists')
    process = CrawlerProcess()
    process.crawl(supermarket.spider)
    process.start()


@click.command()
@click.option('--supermarket', type=click.Choice([name for name in supermarkets.keys()]), help='The supermarket used in the ETL process')
def run(supermarket: str):
    """
    ETL process to save the price through the products time of the main supermarkets of Costa Rica.
    """
    os.makedirs(DATA_DIR, exist_ok=True)

    logger.info("Starting ETL process")

    supermarket: Supermarket = supermarkets[supermarket]

    _extract(supermarket)
    file_paths = TransformSupermarket(supermarket.file_path, supermarket.name).transform()
    SupermarketLoader(file_paths).load()
    
    logger.info('ETL process done')


if __name__ == '__main__':
    run()
