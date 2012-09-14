#!/usr/bin/python
import logging

logging.basicConfig(level=logging.INFO, filename='logfile.txt')

logging.info('Starting program')

logging.info('Trying to divide 1 by 0')

print 1 / 0

logging.info('The division succeeded')

logging.info('Ending program')
