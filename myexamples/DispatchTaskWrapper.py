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
        run_count = defaultdict(str)
        for aTask in tasks:
            if run_count.__contains__(aTask):
                run_count[aTask] += 1
            else:
                run_count[aTask] = 1
            config = th.getConfigValue(aTask,'Time{0:1d}'.format(run_count[aTask]))
            confValue = defaultdict(str)
            confValue['time']=config
            taskClass = th.getTaskClassBy(aTask)
            if preTask==None:
                taskObject = taskClass(FirstDummyWrapperTask(),confValue)
            else:
                taskObject = taskClass(preTask,confValue)
            preTask = taskObject
            print(aTask)
        return [preTask]