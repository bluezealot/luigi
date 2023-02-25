import luigi
from TaskHelper import TaskHelper

class WrapperTask2(luigi.Task):
    pTask = luigi.TaskParameter()
    config = luigi.DictParameter()
    
    def requires(self):
        return [self.pTask]
    
    def setPreviousTask(self, aTask):
        self.pTask = aTask
        
    def output(self):
        return luigi.LocalTarget('data/WrapperTask2_{0}.txt'.format(self.config['time']))
    
    def run(self):
        taskH = TaskHelper()
        with self.output().open('w') as output:
            output.write('I am WrapperTask2\n')
            output.write('My config is'+ taskH.getConfigValue('WrapperTask2', 'TaskSetting'))
        for i in range(0,10):
            print("WrapperTask2:{0:2d}".format(i))