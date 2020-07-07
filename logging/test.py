import logging

logging.basicConfig(level = logging.DEBUG, filename='test.log', format="%(asctime)s :: %(funcName)s :: %(lineno)d :: %(message)s")
logging.debug("this is an debug message")
logging.info("this is an info message")
logging.warning("this is an warning message")
logging.error("this is an error message")
logging.critical("this is ")