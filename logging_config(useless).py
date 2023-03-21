import logging
import os

logging.basicConfig(filename='LogsData/errors.log', encoding='utf-8', format='%(levelname)s : %(message)s (file : %(filename)s - line : %(lineno)d)', level=logging.ERROR)