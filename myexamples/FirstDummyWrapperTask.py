import luigi

class FirstDummyWrapperTask(luigi.WrapperTask):
    def requires(self):
        return []