import numpy as np

data = list(map(lambda x: x.strip().split(),open("Inputs/Day8.txt").readlines()))

#Part1
def antinode_generator(frequency_map, node_map ,frequency, part=1):
    x_coords = np.where(frequency_map == frequency)[0]
    y_coords = np.where(frequency_map == frequency)[1]
    xy_coords = list(zip(y_coords,x_coords))
    for first_coord in xy_coords:
        for second_coord in xy_coords:
            if not first_coord == second_coord:
                inside_x = True
                inside_y = True
                difference = [first_coord[0] - second_coord[0], first_coord[1] - second_coord[1]]
                pos_node = [first_coord[0]+difference[0], first_coord[1]+difference[1]]
                neg_node = [second_coord[0]-difference[0],second_coord[1]-difference[1]]
                if -1 < pos_node[0] < len(antinode_map) and -1 < pos_node[1] < len(antinode_map.transpose()):
                    node_map[pos_node[1]][pos_node[0]] = "#"
                if -1 < neg_node[0] < len(antinode_map) and -1 < neg_node[1] < len(antinode_map.transpose()):
                    node_map[neg_node[1]][neg_node[0]] = "#"
                if part == 2:
                    while inside_x:
                        if -1 < pos_node[0] < len(antinode_map) and -1 < pos_node[1] < len(antinode_map.transpose()):
                            node_map[pos_node[1]][pos_node[0]] = "#"
                            pos_node = [pos_node[0] + difference[0],pos_node[1] + difference[1]]
                        else:
                            inside_x = False
                    while inside_y:
                        if -1 < neg_node[0] < len(antinode_map) and -1 < neg_node[1] < len(antinode_map.transpose()):
                            node_map[neg_node[1]][neg_node[0]] = "#"
                            neg_node = [neg_node[0] - difference[0],neg_node[1] - difference[1]]
                        else:
                            inside_y = False
    return node_map

#Get list of signals, check for doubles to ignore the ones that do not create antinodes
freq = []
double_freq = []
freq_list = []
for line in data:
    new_line = []
    for symbol in line[0]:
        new_line.append(symbol)
        if symbol in freq:
            if symbol not in double_freq:
                double_freq.append(symbol)
        else:
            freq.append(symbol)
    freq_list.append((new_line))
freq_map = np.array(freq_list)
antinode_map = np.full(np.shape(freq_map),".")
for i in double_freq:
    if not i == ".":
        antinode_map = antinode_generator(freq_map, antinode_map, i)
print(f"Part 1 Result: {np.count_nonzero(antinode_map == '#')}")

#Part2
freq_map = np.array(freq_list)
antinode_map = np.full(np.shape(freq_map),"")
for i in double_freq:
    if not i == ".":
        antinode_map = antinode_generator(freq_map, antinode_map, i, part=2)
for y in range(len(antinode_map)):
    for x in range(len(antinode_map)):
        if antinode_map[y,x] == "" and freq_map[x,y] in double_freq:
            antinode_map[y,x] = freq_map[y,x]
print(f"Part 2 Result: {np.shape(antinode_map)[0]*np.shape(antinode_map)[1] - np.count_nonzero(antinode_map == '.')}")
