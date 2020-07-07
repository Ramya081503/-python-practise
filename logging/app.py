import logging

logging.basicConfig(level=logging.DEBUG, filename='test.log', filemode='a',
                    format=" %(funcName)s :: %(lineno)d :: %(message)s")

logging.debug('this is debug message')
logging.info('this is info message')
logging.warning('this is warning message')
logging.error('this is error message')
logging.critical('this is critical message')