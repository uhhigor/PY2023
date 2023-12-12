import logging


class Logger:
    log_level = {
        "DEBUG": 10,
        "INFO": 20,
        "WARNING": 30,
        "ERROR": 40,
        "CRITICAL": 50
    }

    def __init__(self, level: str):
        self.level: int = self.log_level[level]
        file_name = 'chase.log'

        logger = logging.getLogger()
        logger.setLevel(level)

        handler = logging.FileHandler(file_name, 'w')

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        self.logger = logger

    def log(self, level: str, message: str):
        if self.log_level[level] >= self.level:
            self.logger.log(self.log_level[level], message)
