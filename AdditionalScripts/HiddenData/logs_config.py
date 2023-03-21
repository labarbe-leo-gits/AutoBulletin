import logging
import os

info_formatter = logging.Formatter('%(levelname)s : %(message)s')
error_formatter = logging.Formatter('%(levelname)s : %(message)s (file : %(filename)s - line : %(lineno)d)')


def setup_logger(name, log_file, level=logging.DEBUG):
    """To setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(info_formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

def setup_logger_2(name, log_file, level=logging.DEBUG):
    """To setup as many loggers as you want"""

    handler_2 = logging.FileHandler(log_file)        
    handler_2.setFormatter(error_formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler_2)

    return logger

# first file logger - INFO
logger = setup_logger('first_logger', 'LogsData/app.log')

# second file logger - ERROR
super_logger = setup_logger_2('second_logger', 'LogsData/errors.log')
