import logging

"""
logging.DEBUG
logging.INFO
logging.WARNING
logging.ERROR
logging.CRITICAL
"""
format = "%(asctime)s - %(levelname)s : %(pathname)s :: %(message)s"
logging.basicConfig(level=logging.DEBUG, format=format, filename="my_log.txt",
                    filemode="a")

logging.debug("I am debug modified")
logging.info("i amm info modf")
logging.warning("I am warning dfasdf")
logging.error("i am error dfadsf")
logging.critical("I am critical dfasdf")

