data = list(map(lambda x : x.strip(), open("Inputs/Day13.txt").readlines()))

machines = []
for i in data:
    machines.append(i.split())

def calc_count2(B1_x, B1_y, B2_x, B2_y, x, y):
    count2 = (((x*B1_y)/B1_x)-y)/(((B2_x*B1_y)/B1_x)-B2_y)
    return count2

def calc_count1(B1_x, B2_x, c2, x):
    count1 = (x/B1_x)-(B2_x/B1_x)*c2
    return count1

#Part1
i = 0
token_sum = 0
while i < len(machines):
    button1_x = int(machines[i][2][2:-1])
    button1_y = int(machines[i][3][2:])
    button2_x = int(machines[i+1][2][2:-1])
    button2_y = int(machines[i+1][3][2:])
    x_goal = int(machines[i+2][1][2:-1])
    y_goal = int(machines[i+2][2][2:])
    count_b2 = calc_count2(button1_x, button1_y, button2_x, button2_y, x_goal, y_goal)
    count_b1 = calc_count1(button1_x, button2_x, count_b2, x_goal)
    if 0 < count_b1 <= 100 and 0 < count_b2 <= 100 and abs(round(count_b1)-count_b1) < 0.01 and abs(round(count_b2)-count_b2) < 0.01:
        token_sum += round(count_b1)*3+round(count_b2)
    i+=4
print(f"Part 1: {token_sum}")

#Part2
i = 0
token_sum = 0
while i < len(machines):
    button1_x = int(machines[i][2][2:-1])
    button1_y = int(machines[i][3][2:])
    button2_x = int(machines[i+1][2][2:-1])
    button2_y = int(machines[i+1][3][2:])
    x_goal = int(machines[i+2][1][2:-1])+10000000000000
    y_goal = int(machines[i+2][2][2:])+10000000000000
    count_b2 = calc_count2(button1_x, button1_y, button2_x, button2_y, x_goal, y_goal)
    count_b1 = calc_count1(button1_x, button2_x, count_b2, x_goal)
    if abs(round(count_b1)-count_b1) < 0.01 and abs(round(count_b2)-count_b2) < 0.01:
        token_sum += round(count_b1)*3+round(count_b2)
    i+=4
print(f"Part 2: {token_sum}")