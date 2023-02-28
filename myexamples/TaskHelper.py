import configparser

class TaskHelper:
    _config = configparser.ConfigParser()
    def __init__(self):
        self._config.read('config.ini')
    
    # 設定ファイルの内容を読み込みします。
    def getConfigValue(self, taskName, configName):
        config=''
        if self._config.has_option(taskName,configName):
            config = self._config[taskName][configName]
            print(config) 
        return config
    # タスク名によって、対応のタスククラスを取得します。
    def getTaskClassBy(self, taskName):
        module = __import__(taskName)
        class_ = getattr(module, taskName)
        return class_
    