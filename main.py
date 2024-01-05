import logging

logging.basicConfig(level=logging.INFO)

try:
    raise Exception()
except:
    logging.exception("hello world")