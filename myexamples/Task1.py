import luigi

class Task1(luigi.Task):
    def output(self):
        return luigi.LocalTarget('data/task1.txt')
    def run(self):
        with self.output().open('w') as output:
            output.write('I am task1')