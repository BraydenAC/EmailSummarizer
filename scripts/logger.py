import logging
import os
import sys

#Manual config
logging_level = logging.INFO

#The config itself, manual modifications should be done via variables above
logging.basicConfig(
    level = logging_level,
    format = '%(asctime)s|%(levelname)7s|%(name)s',
    datefmt = '%m/%d/Y %H:%M:%S'
)