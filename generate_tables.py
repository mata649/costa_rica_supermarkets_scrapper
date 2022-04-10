from cfg import DB_CONNSTR, SQL_DIR, TABLE_NAMES
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import os
import logging

engine = create_engine(DB_CONNSTR)
logger = logging.getLogger()


def create_tables():
    """Create db tables"""

    with engine.connect() as con:
        for table_name in TABLE_NAMES:
            logger.info(f'Creating table {table_name}')
            with open(os.path.join(SQL_DIR, f'{table_name}.sql')) as f:
                query = text(f.read())
            con.execute(query)


if __name__ == '__main__':
    create_tables()
