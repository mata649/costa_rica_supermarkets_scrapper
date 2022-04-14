from asyncio.log import logger
import os
from hashlib_additional import fletcher32
import pandas as pd

from cfg import CATEGORY_TABLE_NAME, DATA_DIR, PRODUCT_PRICE_TIMELAPSE_TABLE_NAME, PRODUCT_TABLE_NAME, SUPERMARKET_TABLE_NAME


class TransformSupermarket:
    def __init__(self, file_path: str, supermarket_name: str) -> None:
        """
        Object to transform the raw supermarket information, based in a 
        file path to the csv to the raw information.

        Args:
            file_path (str): The file path to the raw information.
            supermarket_name (str): The name of the supermarket which the raw information was obtained
        """
        self.supermarket_name = supermarket_name
        self.products_data_frame = pd.read_csv(file_path)
        self.category_data_frame = None
        self.supermarket_data_frame = None
        self.price_timelapse_data_frame = None
        os.remove(file_path)

    def add_col_id(self, id_col_name: str, col_name: str):
        """ Adds a id column to products data frame, the id
            is generated with the hash algorithm fletcher_32.
        Args:
            id_col_name (str): The name of the id column to add
            col_name (str): The name of the column with the information to encrypt
        """
        # Add id based in the name
        self.products_data_frame[id_col_name] = self.products_data_frame[col_name].apply(
            lambda name: fletcher32(name.encode()).hexdigest())

    def get_data_frame_from_products_data_frame(self, id_col_name: str, col_name: str) -> pd.DataFrame:
        """
            Returns a data frame from products data frame, based in a id column and a column name,
            also will delete the column name specified, leaving the id column as a reference to the new
            data frame.
        Args:
            id_col_name (str): Id column that will be the index in the new data frame.
            col_name (str): The name of the column to save the information in the new data frame.

        Returns:
            pd.DataFrame: The new data frame with the information specified.
        """
        new_data_frame = self.products_data_frame[[id_col_name, col_name]]
        new_data_frame_id = pd.Series(new_data_frame[id_col_name].unique())
        new_data_frame_name = pd.Series(new_data_frame[col_name].unique())
        new_data_frame = pd.concat((new_data_frame_id, new_data_frame_name), axis=1).rename(
            columns={0: 'id', 1: 'name'})
        del self.products_data_frame[col_name]
        return new_data_frame

    def set_supermarket(self):
        """
        Adds the supermarket reference to products data frame.
        """
        self.products_data_frame['supermarket'] = self.supermarket_name
        self.add_col_id(col_name='supermarket', id_col_name='id_supermarket')

    def set_price_timelapse_data_frame(self):
        """
        Adds a reference to product and the price to the price timelapse data frame,
        also deletes the price information from products data frame
        """
        self.price_timelapse_data_frame = self.products_data_frame[[
            'id', 'price']].rename(columns={'id': 'id_product'})
        del self.products_data_frame['price']

    def save_to_csv(self, data_frame: pd.DataFrame, table_name) -> str:
        """ Saves the data frame information in a csv, in the data directory,
            the name of the new csv will be defined for the table name arg.
        Args:
            data_frame (pd.DataFrame): The data frame to save the information in a csv.
            table_name (_type_): The name of the csv to save.

        Returns:
            str: Returns the file path where was saved the csv.
        """
        csv_path = os.path.join(DATA_DIR, f'{table_name}.csv')
        data_frame.to_csv(csv_path, index=False)
        return csv_path

    def remove_duplicates_and_null_fields(self):
        """
        Remove duplicate products in product data frame based on product id.
        Also removes rows with null data
        """
        self.products_data_frame = self.products_data_frame.drop_duplicates(subset=['id'])
        self.products_data_frame = self.products_data_frame.dropna(how='any',axis=0) 


    def transform(self) -> dict:
        """ 
        Transforms and divides the raw information and return 
        a dict with the table_name as key and the file path value
        Returns:
            dict: A dictionary with the file paths to csv with the information
        """
        logger.info('Starting transformation process')
        self.add_col_id(col_name='url', id_col_name='id')
        self.add_col_id(col_name='category', id_col_name='id_category')
        self.remove_duplicates_and_null_fields()
        self.set_supermarket()
        self.category_data_frame = self.get_data_frame_from_products_data_frame(
            id_col_name='id_category', col_name='category')
        self.supermarket_data_frame = self.get_data_frame_from_products_data_frame(
            id_col_name='id_supermarket', col_name='supermarket')
        self.set_price_timelapse_data_frame()

        return{
            SUPERMARKET_TABLE_NAME: self.save_to_csv(self.supermarket_data_frame, SUPERMARKET_TABLE_NAME),
            CATEGORY_TABLE_NAME: self.save_to_csv(self.category_data_frame, CATEGORY_TABLE_NAME),
            PRODUCT_TABLE_NAME: self.save_to_csv(self.products_data_frame, PRODUCT_TABLE_NAME),
            PRODUCT_PRICE_TIMELAPSE_TABLE_NAME: self.save_to_csv(self.price_timelapse_data_frame, PRODUCT_PRICE_TIMELAPSE_TABLE_NAME)}
