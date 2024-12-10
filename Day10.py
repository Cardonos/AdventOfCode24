import numpy as np

data = list(map(lambda x: x.strip(), open("Inputs/Day10.txt").readlines()))

topo_map_list = []
for line in data:
    new_line = []
    for height in line:
        new_line.append(int(height))
    topo_map_list.append(new_line)
topo_map = np.array(topo_map_list)


def check_trails(heightmap, location, current_height, list_of_nines, part2 = False):
    y, x = location
    trail = 0
    if current_height == 9 and location not in list_of_nines:
        if not part2:
            list_of_nines.append(location)
            return 1
        else:
            return 1
    if y + 1 < len(heightmap) and heightmap[y + 1, x] == heightmap[y,x]+1:
        trail += check_trails(heightmap, [y + 1, x], heightmap[y + 1, x], list_of_nines, part2)
    if heightmap[y - 1, x] == heightmap[y,x]+1 and y - 1 >= 0:
        trail += check_trails(heightmap, [y - 1, x], heightmap[y - 1, x], list_of_nines, part2)
    if x + 1 < len(heightmap) and heightmap[y, x + 1] == heightmap[y,x]+1:
        trail += check_trails(heightmap, [y, x + 1], heightmap[y, x + 1], list_of_nines, part2)
    if heightmap[y, x - 1] == heightmap[y,x]+1 and x - 1 >= 0:
        trail += check_trails(heightmap, [y, x - 1], heightmap[y, x - 1], list_of_nines, part2)
    if current_height == 0:
        return trail
    else:
        return trail


trailhead_score_sum = 0
for y, x in list(zip(np.where(topo_map == 0)[0], np.where(topo_map == 0)[1])):
    trailhead_score_sum += check_trails(topo_map, [y,x], 0, [])
print(f"Part 1: {trailhead_score_sum}")


trailhead_rating_sum = 0
for y, x in list(zip(np.where(topo_map == 0)[0], np.where(topo_map == 0)[1])):
    trailhead_rating_sum += check_trails(topo_map, [y,x], 0, [], part2=True)
print(f"Part 2: {trailhead_rating_sum}")