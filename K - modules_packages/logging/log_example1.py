"""
   logging levels:
                DEBUG
                INFO
                WARNING
                ERROR
                CRITICAL
"""


import logging

logging.basicConfig(filename = "test.log", level = logging.DEBUG)
logging.warning("in this we can write a warning messages")
logging.info("in this we can write an information ")
logging.error("in this we can error messages")
