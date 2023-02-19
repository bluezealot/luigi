import luigi
from TaskHelper import TaskHelper
from FirstDummyWrapperTask import FirstDummyWrapperTask
from collections import defaultdict

class DispatchTaskWrapper(luigi.WrapperTask):
    def requires(self):
        th = TaskHelper()
        taskList = th.getConfigValue('DispatchTaskWrapper','TaskList')
        tasks = taskList.split(',')
        preTask = None
        for aTask in tasks:
            taskClass = th.getTaskClassBy(aTask)
            if preTask==None:
                taskObject = taskClass(FirstDummyWrapperTask())
            else:
                taskObject = taskClass(preTask)
            preTask = taskObject
            print(aTask)
        return [preTask]