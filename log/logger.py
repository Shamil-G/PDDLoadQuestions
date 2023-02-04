import logging
from logging.handlers import RotatingFileHandler


def init_logger():
    logger = logging.getLogger('LOADING')
    # logging.getLogger('PDD').addHandler(logging.StreamHandler(sys.stdout))
    # Console
    logging.getLogger('LOADING').addHandler(logging.StreamHandler())
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler("load_questions.log", encoding="UTF-8")
    # fh = RotatingFileHandler(cfg.LOG_FILE, encoding="UTF-8", maxBytes=100000000, backupCount=5)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    logger.info('Logging started')
    return logger


log = init_logger()
