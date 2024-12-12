from helperfuncs import parse_to_2D_map

fence_map = parse_to_2D_map("Inputs/test.txt")
print(fence_map)

dir_dict = [(-1,0), (0, 1), (1, 0), (0, -1)]


def build_fence(garden, location, directions, visited, fence, area, fence_id):
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
                    fence_id.append([curr_area,location, i])
                    fence += 1
                elif [y2, x2] not in visited:
                    fence, area, visited, fence_id = build_fence(garden, [y2, x2], directions, visited, fence, area, fence_id)
            else:
                fence_id.append([curr_area,location,i])
                fence += 1
    return fence, area, visited, fence_id


fence_list = []
#Part1
node_list = []
fence_length = 0
garden_area = 0
garden_area_array = []
price = 0
for y_axis in range(len(fence_map)):
    for x_axis in range(len(fence_map)):
        if [y_axis, x_axis] not in node_list:
            fence_length = 0
            garden_area = 0
            fence_length,garden_area,node_list, fence_list = build_fence(fence_map,[y_axis,x_axis],dir_dict,node_list,fence_length,garden_area, fence_list)
            garden_area_array.append(garden_area)
            price += garden_area * fence_length
print(price)

#Part2

area_edge_list = []
edge_length = []
j = 0
while j < len(fence_list):
    area = fence_list[j][0]
    while j < len(fence_list) and fence_list[j][0] == area:
        area_edge_list.append(fence_list[j])
        j+=1
    j -= 1
    area_edge_list = sorted(area_edge_list)
    a = 0
    checked_edges = []
    for k in area_edge_list:
        check = [[k[0],[k[1][0]+1, k[1][1]] ,k[2]] in checked_edges,
                 [k[0],[k[1][0]-1, k[1][1]] ,k[2]] in checked_edges,
                 [k[0],[k[1][0], k[1][1]+1] ,k[2]] in checked_edges,
                 [k[0],[k[1][0], k[1][1]-1] ,k[2]] in checked_edges]
        if any(check):
            checked_edges.append(k)
        else:
            checked_edges.append(k)
            a += 1
    edge_length.append(a)
    area_edge_list = []
    j+=1

new_price = 0
for ar, ed in list(zip(garden_area_array, edge_length)):
    new_price += ar * ed
print(new_price)
