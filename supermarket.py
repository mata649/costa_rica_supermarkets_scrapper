
from scrapy import Spider
from cfg import RUN_DATE
import os
import pandas as pd


class Supermarket:
    def __init__(self, name: str = None, spider: Spider = None) -> None:
        self.name: str = name
        self.file_path: str = os.path.join('data', f'{name}_{RUN_DATE}.csv')
        self.spider = spider
        self.spider.custom_settings = {
            'FEEDS': {
                self.file_path: {
                    'format': 'csv',
                    'encoding': 'utf-8',
                }
            },
        }
    



class SupermarketException(Exception):
   pass