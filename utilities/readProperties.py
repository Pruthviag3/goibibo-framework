from configparser import ConfigParser

config=ConfigParser()
config.read(".\\Configurations\\config.ini")

class Readconfig:
    @staticmethod
    def appApplicationUrl():
        url=config.get('common info','baseurl')
        return url

    @staticmethod
    def getFromDestinatin():
        fromDestinationTextBox=config.get('common info','fromDestination')
        return fromDestinationTextBox

    @staticmethod
    def getToDestination():
        toDestinationTextBox=config.get('common info','toDestination')
        return toDestinationTextBox

