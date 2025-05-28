import sys
from src.student.logger.loggers import logging
from src.student.exception.exceptions import CustomException

if __name__ == '__main__':
    try:
        logging.info('this the zoro division error')
        1/0
    except Exception as e:
        raise CustomException(e,sys)
    