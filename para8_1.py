import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="logs_p81.log",
                    filemode="w",
                    format="we Have logging message: %(asctime)s:%(levelname)s - %(message)s")

logging.debug("debug")
logging.info("info")
logging.warning("warn")
logging.error("error")
logging.critical("critical")
