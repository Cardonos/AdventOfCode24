import numpy as np
import regex as re

data = list(open("Inputs/Day4.txt"))

#Part1
letter_list = []
for i in data:
    new_line = []
    for j in i.strip():
        new_line.append(j)
    letter_list.append(new_line)
xmas_array = np.array(letter_list)


def shear_list(letters_list):
    new_list = []
    count = 0
    padding = len(letters_list)
    for unpad_line in letters_list:
        padded_line = unpad_line.copy()
        k = 0
        while k < count:
            padded_line.insert(0, "")
            k += 1
        l = 0
        while l < padding:
            padded_line.append("")
            l += 1
        count += 1
        padding -= 1
        new_list.append(padded_line)
    return new_list


left_sheared_array = np.array(shear_list(xmas_array.tolist()))
right_sheared_array = np.array(shear_list(xmas_array.transpose().tolist()))


def check_rows(array):
    count = 0
    for row in array:
        string = "".join(row)
        match = re.findall(r'XMAS|SAMX', string, overlapped=True)
        count += len(match)
    return count


result = check_rows(xmas_array) + check_rows(xmas_array.transpose()) + check_rows(
    left_sheared_array.transpose()) + check_rows(right_sheared_array.transpose())
print(result)

#Part2
c = 0
x_row = 0
for x_row in range(1, len(xmas_array) - 1):
    y_col = 0
    for y_col in range(1, len(xmas_array[0]) - 1):
        if xmas_array[x_row][y_col] == 'A':
            if sorted([xmas_array[x_row - 1][y_col - 1], xmas_array[x_row + 1][y_col + 1]]) == ["M", "S"] and sorted(
                    [xmas_array[x_row - 1][y_col + 1], xmas_array[x_row + 1][y_col - 1]]) == ["M", "S"]:
                c += 1
        y_col += 1
    x_row += 1

print(c)
