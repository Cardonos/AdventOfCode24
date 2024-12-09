data = list(open("Inputs/Day9.txt").read())

#Part1
disk = []
chunked_disk = []
data_or_space = True
data_id = 0
for i in data:
    data_block = []
    c = 0
    if int(i) == 0:
        data_or_space = not data_or_space
        c += 1
        continue
    if data_or_space:
        while c < int(i):
            disk.append(data_id)
            data_block.append(data_id)
            c += 1
        data_id += 1
        data_or_space = False
    else:
        while c < int(i):
            disk.append(".")
            data_block.append(".")
            c += 1
        data_or_space = True
    chunked_disk.append(data_block)

def calc_checksum(datalist):
    checksum = 0
    pos = 0
    for j in datalist:
        if j == ".":
            pos += 1
            continue
        checksum += int(j)*pos
        pos += 1
    return checksum


def bubble_down_individual(datalist):
    left_id = 0
    right_id= len(datalist)-1
    while left_id <= right_id:
        if "." != datalist[left_id]:
            while datalist[right_id] != ".":
                right_id -= 1
            if left_id < right_id:
                datalist[right_id] = datalist[left_id]
                datalist[left_id] = "."
        else:
            left_id += 1
    return datalist

part1 = disk.copy()
part1.reverse()
part1 = bubble_down_individual(part1)
part1.reverse()
print(f"Part 1: {calc_checksum(part1)}")

#Part2
k = 0
print(f"Moving {len(chunked_disk)} blocks of data...")
while k < len(chunked_disk):
    data_index = chunked_disk[len(chunked_disk)-1-k]
    if data_index[0] != ".":
        for l in range(len(chunked_disk)):
            if l >= len(chunked_disk)-1-k:
                break
            if chunked_disk[l][0] == "." and len(data_index) <= len(chunked_disk[l]):
                chunked_disk.insert(l, data_index)
                chunked_disk.pop(len(chunked_disk)-1-k)
                if len(data_index) == len(chunked_disk[l+1]):
                    chunked_disk.insert(len(chunked_disk)-1-k,chunked_disk.pop(l+1))
                else:
                    for _ in range(len(data_index)):
                        if chunked_disk[len(chunked_disk) - 1 - k][0] == '.':
                            chunked_disk[len(chunked_disk) - 1 - k].append(chunked_disk[l+1].pop())
                        else:
                            chunked_disk.insert(len(chunked_disk) - k, [chunked_disk[l+1].pop()])
                break
    k += 1
for_checksum = []
for m in chunked_disk:
    for n in m:
        for_checksum.append(n)
print(f"Part 2: {calc_checksum(for_checksum)}")