import logging
import os
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
if __name__ == '__main__':
    logger.info(os.getcwd())