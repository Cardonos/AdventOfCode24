import numpy as np

data = open("Inputs/Day15.txt").readlines()
print(data)
warehouse_list = []
commands = []
for line in data:
    if  line[0] == "#":
        new_line = []
        for symbol in line.strip():
            new_line.append(symbol)
        warehouse_list.append(new_line)
    else:
        commands += line.strip()

warehouse = np.array(warehouse_list)
dir_dict = {"^":(-1,0), ">":(0, 1), "v":(1, 0), "<":(0, -1)}


def print_map(w_map: dict):
    print()
    for py in range(np.shape(w_map)[0]):
        print_line = ''
        for px in range(np.shape(w_map)[1]):
            c = w_map[(py, px)]
            if c == '#':
                c = '⬜️'
            elif c == '.':
                c = '⬛'
            elif c in 'O[':
                c = '📦'
            elif c == ']':
                c = '🎁'
            elif c == '@':
                c = '🤖'
            print_line += c
        print(print_line)
    print()


def move(warehouse_map1 ,direction, current_loc, robot_or_box="@"):
    y_move, x_move = dir_dict[direction]
    y, x = current_loc
    moved = False
    new_loc = warehouse_map1[y + y_move,x + x_move]
    if new_loc == "#":
        return moved, warehouse_map1
    elif new_loc == "O":
        moved, warehouse_map = move(warehouse_map1, direction, [y+y_move, x+x_move], robot_or_box="O")
        if moved:
            warehouse_map[y+y_move, x+x_move] = robot_or_box
            warehouse_map[y,x] = "."
    else:
        moved = True
        warehouse_map1[y + y_move,x + x_move] = robot_or_box
        warehouse_map1[y,x] = "."
    return moved, warehouse_map1


def move_wide_box(warehouse_map, direction, location, side):
    y_move,x_move = dir_dict[direction]
    y, x = location
    moved = False
    #differentiate cases
    #split push can only occur when pushing up or down
    #left right can be ignored, only needs to be chained
    if direction == "<" or direction == ">":
        if side == "[":
            new_loc = warehouse_map[y,x+2]
            if new_loc == "#":
                return False, warehouse_map
            if new_loc == ".":
                warehouse_map[y,x] = "."
                warehouse_map[y,x+1] = "["
                warehouse_map[y,x+2] = "]"
                moved = True
            if new_loc == "[":
                moved, warehouse_map = move_wide_box(warehouse_map.copy(), direction, [y,x+2], "[")
                if moved:
                    warehouse_map[y,x] = "."
                    warehouse_map[y,x + 1] = "["
                    warehouse_map[y,x + 2] = "]"
                    moved = True
        else:
            new_loc = warehouse_map[y,x-2]
            if new_loc == "#":
                return False, warehouse_map
            if new_loc == ".":
                warehouse_map[y,x] = "."
                warehouse_map[y,x-2] = "["
                warehouse_map[y,x-1] = "]"
                moved = True
            if new_loc == "]":
                moved,warehouse_map = move_wide_box(warehouse_map.copy(),direction,[y,x-2],"]")
                if moved:
                    warehouse_map[y,x] = "."
                    warehouse_map[y,x - 2] = "["
                    warehouse_map[y,x - 1] = "]"
                    moved = True
    else:
        if side == "[":
            if warehouse_map[y+y_move,x] == "." and warehouse_map[y+y_move, x+1] == ".":
                warehouse_map[y+y_move,x] = "["
                warehouse_map[y+y_move,x+1] = "]"
                warehouse_map[y,x] = "."
                warehouse_map[y,x+1] = "."
                moved = True
            # case 1: box on box
            elif warehouse_map[y+y_move,x] == "[":
                moved, warehouse_map = move_wide_box(warehouse_map.copy(), direction, [y+y_move,x], "[")
                if moved:
                    warehouse_map[y + y_move,x] = "["
                    warehouse_map[y + y_move,x + 1] = "]"
                    warehouse_map[y,x] = "."
                    warehouse_map[y,x + 1] = "."
                    moved = True
            #case 2: offset box
            elif warehouse_map[y+y_move,x] == "]" and not warehouse_map[y+y_move, x+1] == "[":
                moved,warehouse_map = move_wide_box(warehouse_map.copy(),direction,[y + y_move,x],"]")
                if moved:
                    warehouse_map[y + y_move,x] = "["
                    warehouse_map[y + y_move,x + 1] = "]"
                    warehouse_map[y,x] = "."
                    warehouse_map[y,x + 1] = "."
                    moved = True
            elif not warehouse_map[y + y_move,x] == "]" and warehouse_map[y + y_move,x + 1] == "[":
                moved,warehouse_map = move_wide_box(warehouse_map.copy(),direction,[y + y_move,x+1],"[")
                if moved:
                    warehouse_map[y + y_move,x] = "["
                    warehouse_map[y + y_move,x + 1] = "]"
                    warehouse_map[y,x] = "."
                    warehouse_map[y,x + 1] = "."
                    moved = True
            #case 3: double box on box
            elif warehouse_map[y + y_move,x] == "]" and warehouse_map[y + y_move,x + 1] == "[":
                moved1, warehouse_map1 = move_wide_box(warehouse_map.copy(),direction,[y + y_move,x],"]")
                moved2, warehouse_map2 = move_wide_box(warehouse_map1.copy(),direction,[y + y_move,x+1],"[")
                if all([moved1,moved2]):
                    warehouse_map = warehouse_map2
                    warehouse_map[y + y_move,x] = "["
                    warehouse_map[y + y_move,x + 1] = "]"
                    warehouse_map[y,x] = "."
                    warehouse_map[y,x + 1] = "."
                    moved = True
        elif side == "]":
            if warehouse_map[y+y_move,x] == "." and warehouse_map[y+y_move, x-1] == ".":
                warehouse_map[y+y_move,x-1] = "["
                warehouse_map[y+y_move,x] = "]"
                warehouse_map[y,x-1] = "."
                warehouse_map[y,x] = "."
                moved = True
            # case 1: box on box
            elif warehouse_map[y+y_move,x] == "]":
                moved, warehouse_map = move_wide_box(warehouse_map.copy(), direction, [y+y_move,x], "]")
                if moved:
                    warehouse_map[y + y_move,x] = "]"
                    warehouse_map[y + y_move,x -1] = "["
                    warehouse_map[y,x-1] = "."
                    warehouse_map[y,x] = "."
                    moved = True
            # case 2: offset box
            elif warehouse_map[y + y_move,x] == "[" and not warehouse_map[y + y_move,x-1] == "]":
                moved,warehouse_map = move_wide_box(warehouse_map.copy(),direction,[y + y_move,x],"[")
                if moved:
                    warehouse_map[y + y_move,x-1] = "["
                    warehouse_map[y + y_move,x] = "]"
                    warehouse_map[y,x-1] = "."
                    warehouse_map[y,x] = "."
                    moved = True
            elif not warehouse_map[y + y_move,x] == "[" and warehouse_map[y + y_move,x - 1] == "]":
                moved,warehouse_map = move_wide_box(warehouse_map.copy(),direction,[y + y_move,x-1],"]")
                if moved:
                    warehouse_map[y + y_move,x-1] = "["
                    warehouse_map[y + y_move,x] = "]"
                    warehouse_map[y,x-1] = "."
                    warehouse_map[y,x] = "."
                    moved = True
            # case 3: double box on box
            elif warehouse_map[y + y_move,x] == "[" and warehouse_map[y + y_move,x - 1] == "]":
                moved1,warehouse_map1 = move_wide_box(warehouse_map.copy(),direction,[y + y_move,x],"[")
                moved2,warehouse_map2 = move_wide_box(warehouse_map1.copy(),direction,[y + y_move,x-1],"]")
                if all([moved1,moved2]):
                    warehouse_map = warehouse_map2
                    warehouse_map[y + y_move,x-1] = "["
                    warehouse_map[y + y_move,x] = "]"
                    warehouse_map[y,x-1] = "."
                    warehouse_map[y,x] = "."
                    moved = True
    return moved, warehouse_map

def wide_move(warehouse_map ,direction, current_loc, robot_or_box="@"):
    y_move, x_move = dir_dict[direction]
    y, x = current_loc
    moved = False
    new_loc = warehouse_map[y + y_move,x + x_move]
    if new_loc == "#":
        return moved, warehouse_map
    elif new_loc == "[" or new_loc == "]":
        moved, warehouse_map = move_wide_box(warehouse_map.copy(), direction, [y+y_move, x+x_move], warehouse_map[y+y_move,x+x_move])
        if moved:
            warehouse_map[y+y_move, x+x_move] = robot_or_box
            warehouse_map[y,x] = "."
    else:
        moved = True
        warehouse_map[y + y_move,x + x_move] = robot_or_box
        warehouse_map[y,x] = "."
    return moved, warehouse_map

def GPS(warehouse_map2, part2=False):
    box = "O"
    if part2:
        box = "["
    sum_gps = 0
    for y in range(len(warehouse_map2)):
        for x in range(len(warehouse_map2.transpose())):
            if warehouse_map2[y,x] == box:
                sum_gps += (100*y)+x
    return sum_gps

#Part1
new_warehouse = warehouse.copy()
for i in commands:
    _, new_warehouse = move(new_warehouse, i, list(np.where(new_warehouse == "@")))
print(f"Part 1: {GPS(new_warehouse)}")

#Part2

#translate to new map:
wide_warehouse_list = []
for i in range(len(warehouse)):
    new_wide_line = []
    for j in range(len(warehouse.transpose())):
        part = warehouse[i,j]
        if part == "@":
            new_wide_line.append(part)
            new_wide_line.append(".")
        elif part == "O":
            new_wide_line.append("[")
            new_wide_line.append("]")
        else:
            new_wide_line.append(part)
            new_wide_line.append(part)
    wide_warehouse_list.append(new_wide_line)
wide_warehouse = np.array(wide_warehouse_list)

for i in commands:
    _, wide_warehouse = wide_move(wide_warehouse.copy(), i, list(np.where(wide_warehouse == "@")))
print_map(wide_warehouse)

print(GPS(wide_warehouse, part2=True))
