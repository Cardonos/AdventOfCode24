import numpy as np

raw_data = list(open("Inputs/Day2.txt"))
data = []
for string in raw_data:
    data.append(list(map(int, string.split())))
#Part1
def check_safe(row):
    is_safe = False
    is_increasing = []
    is_decreasing = []
    for i in range(len(row)-1):
        if 1 <= row[i] - row[i+1] <= 3:
            is_decreasing.append(True)
        else:
            is_decreasing.append(False)
        if 1 <= row[i+1] - row[i] <= 3:
            is_increasing.append(True)
        else:
            is_increasing.append(False)
    if all(is_increasing) or all(is_decreasing):
        is_safe = True
    return is_safe

all_safe = []
for j in data:
    all_safe.append(check_safe(j))
print(all_safe.count(True))

#Part2
def check_safe_2(row):
    is_safe = []
    for i in range(len(row)):
        one_removed = row.copy()
        one_removed.pop(i)
        is_safe.append(check_safe(one_removed))
    return any(is_safe)

all_safe = []
for j in data:
    all_safe.append(check_safe_2(j, False))
print(all_safe.count(True))
