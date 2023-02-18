import luigi
from Task1 import Task1

class Task2(luigi.Task):
    def requires(self):
        module = __import__('Task1')
        class_ = getattr(module, 'Task1')
        return [class_()]
    def output(self):
        return luigi.LocalTarget('data/task2.txt')
    def run(self):
        with self.output().open('w') as output:
            output.write('I am task2')