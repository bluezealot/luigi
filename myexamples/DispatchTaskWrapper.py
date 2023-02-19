import luigi
from TaskHelper import TaskHelper

class DispatchTaskWrapper(luigi.WrapperTask):
    def requires(self):
        th = TaskHelper();
        for i in range(0,3):
            th.getConfigValue();
            yield 