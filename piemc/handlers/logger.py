import logging
import os
import piemc.config  # Assuming you have a config module with LOG_LEVEL defined

def create_logger(name):
    log_level_mapping = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }
    log_level = log_level_mapping.get(piemc.config.LOG_LEVEL.upper(), logging.INFO)
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    log_dir = './log'
    os.makedirs(log_dir, exist_ok=True)  # Create the directory if it doesn't exist

    log_file = os.path.join(log_dir, name + '.log')
    fhandler = logging.FileHandler(log_file, 'w', 'utf-8')
    shandler = logging.StreamHandler()

    formatter = logging.Formatter(
        "[%(name)s]" + str(' ' * (11 - len(name))) + "[%(asctime)s] [%(levelname)s] : %(message)s")
    fhandler.setFormatter(formatter)
    shandler.setFormatter(formatter)

    logger.addHandler(fhandler)
    logger.addHandler(shandler)

    return logger