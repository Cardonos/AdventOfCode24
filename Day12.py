from helperfuncs import parse_to_2D_map

fence_map = parse_to_2D_map("Inputs/test.txt")
print(fence_map)

dir_dict = [(-1,0), (0, 1), (1, 0), (0, -1)]


def build_fence(garden, location, directions, visited, fence, area):
    if location not in visited:
        area += 1
        y, x = location
        visited.append([y, x])
        curr_area = garden[y, x]

        for i in directions:
            y_dir, x_dir = i
            y2 = y+y_dir
            x2 = x+x_dir
            if -1 < y2 < len(garden) and -1 < x2 < len(garden):
                if not garden[y2, x2] == curr_area:
                        fence += 1
                elif [y2, x2] not in visited:
                    fence, area, visited = build_fence(garden, [y2, x2], directions, visited, fence, area)
            else:

                    fence += 1
    return fence, area, visited



#Part1
node_list = []
fence_length = 0
garden_area = 0
price = 0
for y_axis in range(len(fence_map)):
    for x_axis in range(len(fence_map)):
        if [y_axis, x_axis] not in node_list:
            fence_length = 0
            garden_area = 0
            fence_length,garden_area,node_list = build_fence(fence_map,[y_axis,x_axis],dir_dict,node_list,fence_length,garden_area)
            price += garden_area * fence_length
print(price)

#Part2

