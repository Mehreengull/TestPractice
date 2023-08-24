from configparser import ConfigParser


def read_configurations (category, key):
    config = ConfigParser()
    config.read("C:\Mehreen\Automation_work\GoogleSearch\configurations\config.ini")
    return config.get(category, key)
