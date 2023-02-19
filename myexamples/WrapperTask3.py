import luigi
from TaskHelper import TaskHelper

class WrapperTask3(luigi.Task):
    pTask = luigi.TaskParameter()
    config = luigi.DictParameter()

    def requires(self):
        return [self.pTask]
    
    def setPreviousTask(self, aTask):
        self.pTask = aTask

    def output(self):
        return luigi.LocalTarget('data/WrapperTask3_{0:2d}.txt'.format(self.config['time']))
    
    def run(self):
        taskH = TaskHelper()
        with self.output().open('w') as output:
            output.write('I am WrapperTask3\n')
            output.write('My config is'+ taskH.getConfigValue('WrapperTask3', 'TaskSetting'))
        for i in range(0,10):
            print("WrapperTask3:{0:2d}".format(i))