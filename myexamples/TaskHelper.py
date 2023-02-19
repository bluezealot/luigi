import configparser

class TaskHelper:
    _config = configparser.ConfigParser()
    def __init__(self):
        self._config.read('config.ini')
        
    def getConfigValue(self, taskName, configName):
        config=''
        if self._config.has_option(taskName,configName):
            config = self._config[taskName][configName]
            print(config) 
        return config
    
    def getTaskClassBy(self, taskName):
        module = __import__(taskName)
        class_ = getattr(module, taskName)
        return class_
    