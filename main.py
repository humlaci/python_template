#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module docstring."""

# Imports
from my_logger import logger
from dotenv import dotenv_values
from dotenv import load_dotenv

# Module Constants

# Module "Global" Variables

# .env
config = dotenv_values()
load_dotenv()

# Module Functions and Classes

def main(*args):
    """Program execution starts here."""
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
# Check to see if this file is the "__main__" script being executed
if __name__ == '__main__':
    main()
