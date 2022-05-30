
import csv


def load_road_network(filename):

    def path_cost(path, intersection, road_times):
        def parse(file):
            d = {}
            with open(file) as f:
                r = csv.DictReader(f)
                for line in r:
                    id = line.pop('id')
                    d.update({id: line})
            return d
load_road_network("road_file2.txt")    