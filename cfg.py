from datetime import datetime
import os
from decouple import AutoConfig

ROOT_DIR = os.getcwd()
SQL_DIR = os.path.join(ROOT_DIR, 'sql_scripts')

RUN_DATE = datetime.today().strftime('%d_%m_%Y')
config = AutoConfig(search_path=ROOT_DIR)
DB_CONNSTR = config('DB_CONNSTR')

# Tables Names

PRODUCTS_TABLE_NAME = 'products'
SUPERMARKETS_TABLE_NAME = 'supermarkets'
CATEGORIES_TABLE_NAME = 'categories'
PRODUCT_PRICE_TIMELAPSE = 'products_prices_timelapse'

TABLE_NAMES = [CATEGORIES_TABLE_NAME, SUPERMARKETS_TABLE_NAME, PRODUCTS_TABLE_NAME,
               PRODUCT_PRICE_TIMELAPSE]
