import luigi
from TaskHelper import TaskHelper

class DispatchTask(luigi.Task):
    def requires(self):
        taskH = TaskHelper()
        config = taskH.getConfigValue('DispachTask','DependOn')
        class_ = taskH.getTaskClassBy(config)
        return [class_()]
    
    def output(self):
        return luigi.LocalTarget('data/DispachTask.txt')
    
    def run(self):
        taskH = TaskHelper()
        with self.output().open('w') as output:
            output.write('I am DispachTask\n')
            output.write('My config is'+ taskH.getConfigValue('DispachTask', 'TaskSetting'))