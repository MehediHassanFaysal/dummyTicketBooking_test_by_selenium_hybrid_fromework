import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")  # read the date from config.ini file

class ReadConfig():

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

