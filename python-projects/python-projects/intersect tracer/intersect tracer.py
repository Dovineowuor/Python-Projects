def data_dictionary(filename):
    
    d = {}
    for i in range(len(keys)):
        d[keys[i]] = values[i]
    return d


def parse(file):

    d = {}
    with open(file) as file_name:
        for line in file_name:
            keys = (item.strip() for item in line.split(','))
        for line in file_name:
            values = (item.strip() for item in line.split('/n'))
            data_dictionary(keys,values)
            return d
            
data_dictionar("road_sample2.txt")