import logging

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)
FORMAT = "%(levelname)s: [%(filename)s:%(lineno)s - %(funcName)20s()] %(message)s"
formatter = logging.Formatter(FORMAT)
stream_hander = logging.StreamHandler()
stream_hander.setFormatter(formatter)
logger.addHandler(stream_hander)


