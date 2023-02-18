import luigi
from Streams import Streams
from collections import defaultdict

class AggregateArtists(luigi.Task):
    """
    This task runs over the target data returned by :py:meth:`~/.Streams.output` and
    writes the result into its :py:meth:`~.AggregateArtists.output` target (local file).
    """

    date_interval = luigi.DateIntervalParameter()

    def output(self):
        """
        Returns the target output for this task.
        In this case, a successful execution of this task will create a file on the local filesystem.

        :return: the target output for this task.
        :rtype: object (:py:class:`luigi.target.Target`)
        """
        return luigi.LocalTarget("data/artist_streams_{}.tsv".format(self.date_interval))

    def requires(self):
        """
        This task's dependencies:

        * :py:class:`~.Streams`

        :return: list of object (:py:class:`luigi.task.Task`)
        """
        print("Aggregate requires")
            
        return [Streams(date) for date in self.date_interval]

    def run(self):
        artist_count = defaultdict(int)

        for t in self.input():
            with t.open('r') as in_file:
                for line in in_file:
                    _, artist, track = line.strip().split()
                    artist_count[artist] += 1

        with self.output().open('w') as out_file:
            for artist, count in artist_count.items():
                out_file.write('{}\t{}\n'.format(artist, count))

if __name__ == "__main__":
    luigi.run()
