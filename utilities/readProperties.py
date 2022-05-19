import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations/config.ini")


class ReadConfig:
    @staticmethod
    def getWebURL():
        url = config.get('variables', 'baseURL')
        return url
