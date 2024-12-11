data = open("Inputs/Day11.txt").read().strip().split()

first_dict = {}
for i in data:
    first_dict[i] = 1
second_dict = first_dict.copy()


def mut(dictlist):
    changed_dict = {}
    for j in dictlist:
        l = int(dictlist[j])
        digits = len(j)
        if int(j) == 0:
            if "1" in changed_dict:
                changed_dict["1"] = changed_dict["1"]+l
            else:
                changed_dict["1"] = l
        elif digits % 2 == 0:
            halflen = int(len(j) / 2)
            s1 = int(j[:halflen])
            s2 = int(j[halflen:])
            if str(s1) in changed_dict:
                changed_dict[str(s1)] = changed_dict[str(s1)]+l
            else:
                changed_dict[str(s1)] = l
            if str(s2) in changed_dict:
                changed_dict[str(s2)] = changed_dict[str(s2)]+l
            else:
                changed_dict[str(s2)] = l
        else:
            k = str(int(j)*2024)
            if k in changed_dict:
                changed_dict[k] = changed_dict[k]+l
            else:
                changed_dict[k] = l
    return changed_dict

#Part1

for _ in range(25):
    first_dict = mut(first_dict)
print(f"Part 1: {sum(first_dict.values())}")

#Part2
for _ in range(75):
    second_dict = mut(second_dict)
print(f"Part 2: {sum(second_dict.values())}")
