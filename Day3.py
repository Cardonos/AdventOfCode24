import re
data = open("Inputs/Day3.txt").read()

#Part1
match = re.findall("mul\(\d{1,3},\d{1,3}\)", data)
result = 0
for i in match:
    find_number = re.findall("\d{1,3}", i)
    result += int(find_number[0])*int(find_number[1])
print(result)

#Part2
cleaned_in = re.sub(r"don't\(\).*?(?:do\(\)|$)", "", data, flags=re.DOTALL)
result_clean = 0
match_do = re.findall("mul\(\d{1,3},\d{1,3}\)", cleaned_in)
for j in match_do:
    find_number = re.findall("\d{1,3}",j)
    result_clean += int(find_number[0]) * int(find_number[1])
print(result_clean)