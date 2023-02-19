import luigi
from TaskHelper import TaskHelper

class WrapperTask1(luigi.Task):
    pTask = None
    
    def setPreviousTask(self, aTask):
        self.pTask = aTask
        
    def requires(self):
        return [self.pTask]
    
    def output(self):
        return luigi.LocalTarget('data/WrapperTask1.txt')
    
    def run(self):
        taskH = TaskHelper()
        with self.output().open('w') as output:
            output.write('I am WrapperTask1\n')
            output.write('My config is'+ taskH.getConfigValue('WrapperTask1', 'TaskSetting'))
        for i in range(0,10):
            print("WrapperTask1:{0:2d}".format(i))