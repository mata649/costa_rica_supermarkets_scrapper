
from spiders.pricesmart_spider import PriceSmartSpider
from spiders.pequeno_mundo_spider import PequenoMundoSpider
from supermarket import Supermarket
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


supermarkets = [
    Supermarket(name='pequeno_mundo', spider=PequenoMundoSpider),
    Supermarket(name='pricesmart', spider=PriceSmartSpider)
]
process = CrawlerProcess()

def _extract():
    logger.info('Starting extraction process')

    # for supermarket in supermarkets:
    #     process.crawl(supermarket.spider)
    #     process.crawl(supermarket.spider)
    process.crawl(supermarkets[0].spider)
    process.crawl(supermarkets[1].spider)
    
    
    process.start()
    

   


def run():
    _extract()


if __name__ == '__main__':
    logger.info("Starting ETL process")
    run()
