#!/usr/bin/python
from ConfigParser import ConfigParser

CONFIGFILE = "python.txt"

config = ConfigParser()
config.read(CONFIGFILE)

print config.get('message', 'greeting')

radius = input(config.get('message', 'question') + ' ')

print config.get('message', 'result_message'),

print config.getfloat('numbers', 'pi') * radius**2
