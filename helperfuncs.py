import numpy as np


def parse_to_2D_map(filepath):
    data = open(filepath).read().strip().split()
    listmap = []
    for i in data:
        new_line = []
        for j in i:
            new_line.append(j)
        listmap.append(new_line)
    array_map = np.array(listmap)
    return array_map
