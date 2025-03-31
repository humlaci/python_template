#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module docstring."""

# Imports
import my_logger
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
    my_logger.logger.debug('This is a debug message')
    my_logger.logger.info('This is an info message')
    my_logger.logger.warning('This is a warning message')
    my_logger.logger.error('This is an error message')
    my_logger.logger.critical('This is a critical message')
# Check to see if this file is the "__main__" script being executed
if __name__ == '__main__':
    main()