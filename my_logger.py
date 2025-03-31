#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module docstring."""

# Imports
from dotenv import load_dotenv
from dotenv import dotenv_values
import os
import logging

# Module Constants


# Module "Global" Variables

# .env
config = dotenv_values()
load_dotenv()

# Create a logger
logger = logging.getLogger(__name__)

# Set logger level to DEBUG - This should always be DEBUG
# If this is not DEBUG, and one of the handlers are DEBUG -> DEBUG type messages will not be logged
logger.setLevel(logging.DEBUG)

# Formatter
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(module)s - Line:%(lineno)d - %(message)s')
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(module)s - Line:%(lineno)d - %(message)s')

# Logging to Console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(console_formatter)

# Logging to File
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(file_formatter)



# Add handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Module Functions and Classes
def main(*args):
    """Program execution starts here."""
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
		
    #print(os.getenv('DOMAIN'))
    #print(config['DOMAIN'])

# Check to see if this file is the "__main__" script being executed
if __name__ == '__main__':
    main()