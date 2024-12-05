data = open("Inputs/Day5.txt").readlines()

#Part1
i = 0
while i < len(data):
    data[i] = data[i].strip()
    i+=1
rules = data[0:(data.index(""))]
printlist = data[(data.index(""))+1:len(data)]

rules_list = []
for i in rules:
    rules_list.append(i.split('|'))
middle_number_sum = 0
incorrect_list = []
for i in printlist:
    page_order = i.split(',')
    in_order = True
    for j in rules_list:
        try:
            min_index = page_order.index(j[0])
            if min_index > page_order.index(j[1]):
                in_order = False

        except:
            continue
    if in_order:
        middle_number_sum += int(page_order[int(len(page_order)/2)])
    else:
        incorrect_list.append(page_order)
print(middle_number_sum)

#Part2
ordered_middle_sum = 0
for k in incorrect_list:
    correct_sort = False
    sorted_row = k
    while not correct_sort:
        correct_sort = True
        for l in rules_list:
            try:
                min_index = sorted_row.index(l[0])
                checked = sorted_row.index(l[1])
                if min_index > checked:
                    sorted_row.pop(checked)
                    sorted_row.insert(min_index,l[1])
            except:
                continue
        for l in rules_list:
            try:
                min_index = sorted_row.index(l[0])
                checked = sorted_row.index(l[1])
                if min_index > checked:
                    correct_sort = False
            except:
                continue
        if correct_sort:
            ordered_middle_sum += int(sorted_row[int(len(sorted_row) / 2)])

print(ordered_middle_sum)

