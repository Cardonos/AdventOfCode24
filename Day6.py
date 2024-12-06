import numpy as np
import time
data = open("Inputs/Day6.txt").readlines()

#Part1
map_list = []
for i in data:
    map_list.append([*i.strip()])
lab_map = np.array(map_list)

rotation = ['^', ">", "v", "<"]
rotation_index = 0

def move(lab, y, x, rot_index):
    if rotation[rot_index] == "^":
        y_ax=-1
        x_ax=0
    elif rotation[rot_index] == ">":
        y_ax=0
        x_ax=1
    elif rotation[rot_index] == "<":
        y_ax=0
        x_ax=-1
    elif rotation[rot_index] == "v":
        y_ax=1
        x_ax=0

    new_y = y+y_ax
    new_x = x+x_ax
    if new_y == len(lab) or new_y == -1 or new_x == len(lab.transpose()) or new_x == -1:
        lab[y,x] = "X"
        return lab, new_y, new_x, rot_index

    if lab[new_y, new_x] == "#":
        new_rot_index = (rot_index+1)%4
        lab[y,x] = rotation[new_rot_index]
        return lab, y, x,new_rot_index
    else:
        lab[new_y,new_x] = rotation[rot_index]
        lab[y,x] = "X"
        return lab,new_y,new_x,rot_index

y, x = np.where(lab_map == "^")
guard_track = lab_map.copy()
steps = 0
while -1 < y < len(lab_map) and -1 < x < len(lab_map.transpose()):
    steps += 1
    guard_track, y, x, rotation_index = move(guard_track, y,x, rotation_index)
result1 = np.count_nonzero(guard_track == "X")

#Part2
blocked_paths_xy = []
for i in range(steps-1):
    #print(f"Step {i+1} of {steps-1}")
    y,x = np.where(lab_map == "^")
    rotation_index = 0
    blocked_map = lab_map.copy()

    check_y,check_x = np.where(lab_map == "^")
    block_path_map = lab_map.copy()
    block_rot_index = rotation_index
    for j in range(i):
        block_path_map,check_y,check_x,block_rot_index = move(block_path_map,check_y,check_x,block_rot_index)

    if rotation[block_rot_index] == "^":
        ybloc=-1
        xbloc=0
    elif rotation[block_rot_index] == ">":
        ybloc=0
        xbloc=1
    elif rotation[block_rot_index] == "<":
        ybloc=0
        xbloc=-1
    elif rotation[block_rot_index] == "v":
        ybloc=1
        xbloc=0

    new_bloc = (check_y+ybloc,check_x+xbloc)
    blocked_map[new_bloc] = "#"
    count = 0

    while -1 < check_y < len(lab_map) and -1 < check_x < len(lab_map.transpose()):
        if count == 10000:
            if new_bloc not in blocked_paths_xy:
                blocked_paths_xy.append(new_bloc)
            break
        blocked_map,check_y,check_x,block_rot_index = move(blocked_map,check_y,check_x,block_rot_index)
        count += 1

print(len(blocked_paths_xy))