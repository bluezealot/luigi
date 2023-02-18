import luigi
from Task2 import Task2

class Task3(luigi.Task):
    def requires(self):
        module = __import__('Task1')
        class_ = getattr(module, 'Task1')
        return [class_()]
    def output(self):
        return luigi.LocalTarget('data/task3.txt')
    def run(self):
        print('Running task3')
        with self.output().open('w') as output:
            output.write('I am task3')