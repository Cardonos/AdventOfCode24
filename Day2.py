raw_data = list(open("Inputs/Day2.txt"))
data = []
for string in raw_data:
    data.append(list(map(int, string.split())))
#Part1
def check_safe(row):
    is_safe = []
    if row[0] - row[1] > 0:
        for i in range(len(row)-1):
            if 1 <= row[i] - row[i+1] <= 3:
                is_safe.append(True)
            else:
                is_safe.append(False)
    else:
        for i in range(len(row) - 1):
            if 1 <= row[i+1] - row[i] <= 3:
                is_safe.append(True)
            else:
                is_safe.append(False)
    return all(is_safe)

all_safe = []
for j in data:
    all_safe.append(check_safe(j))
print(all_safe.count(True))

#Part2
def check_safe_2(row):
    is_safe = []
    for k in range(len(row)):
        one_removed = row.copy()
        one_removed.pop(k)
        is_safe.append(check_safe(one_removed))
    return any(is_safe)

all_safe = []
for l in data:
    all_safe.append(check_safe_2(l))
print(all_safe.count(True))
