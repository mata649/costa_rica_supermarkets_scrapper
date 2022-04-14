from datetime import datetime
import os
from decouple import AutoConfig

ROOT_DIR = os.getcwd()
DATA_DIR = os.path.join(ROOT_DIR, 'data')
RUN_DATE = datetime.today().strftime('%d_%m_%Y')
config = AutoConfig(search_path=ROOT_DIR)
DB_CONNSTR = config('DB_CONNSTR')

# Tables Names

PRODUCT_TABLE_NAME = 'product'
SUPERMARKET_TABLE_NAME = 'supermarket'
CATEGORY_TABLE_NAME = 'category'
PRODUCT_PRICE_TIMELAPSE_TABLE_NAME = 'product_price_timelapse'
