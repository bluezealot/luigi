import luigi
from TaskHelper import TaskHelper


class Task2(luigi.Task):
    def requires(self):
        taskH = TaskHelper()
        config = taskH.getConfigValue('Task2','DependOn')
        if not config:
            return None
        class_ = taskH.getTaskClassBy(config)
        return [class_()]
    
    def output(self):
        return luigi.LocalTarget('data/task2.txt')
    
    def run(self):
        taskH = TaskHelper()
        with self.output().open('w') as output:
            output.write('I am task2\n')
            output.write('My config is'+ taskH.getConfigValue('Task2', 'TaskSetting'))