import luigi
from TaskHelper import TaskHelper

class DispatchTaskWrapper(luigi.WrapperTask):
    def requires(self):
        th = TaskHelper()
        taskList = th.getConfigValue('DispatchTaskWrapper','TaskList')
        tasks = taskList.split(',')
        for aTask in tasks:
            taskClass = th.getTaskClassBy(aTask)
            yield taskClass()
            print(aTask)