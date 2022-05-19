import logging


class TestLog:
    @staticmethod
    def CreateLog():
        logging.basicConfig()
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        FileHanlder = logging.FileHandler('.\\Logs\\testlogs.log')
        logger.addHandler(FileHanlder)
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        FileHanlder.setFormatter(formatter)
        logger.addHandler(FileHanlder)

        return logger
