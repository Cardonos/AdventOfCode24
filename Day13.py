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

def calc_token_sum(machine_list, part2=False):
    i = 0
    token_sum = 0
    while i < len(machine_list):
        button1_x = int(machine_list[i][2][2:-1])
        button1_y = int(machine_list[i][3][2:])
        button2_x = int(machine_list[i + 1][2][2:-1])
        button2_y = int(machine_list[i + 1][3][2:])
        x_goal = int(machine_list[i + 2][1][2:-1])
        y_goal = int(machine_list[i + 2][2][2:])
        if part2:
            x_goal += 10000000000000
            y_goal += 10000000000000
        count_b2 = calc_count2(button1_x, button1_y, button2_x, button2_y, x_goal, y_goal)
        count_b1 = calc_count1(button1_x, button2_x, count_b2, x_goal)
        if part2:
            if abs(round(count_b1) - count_b1) < 0.01 and abs(round(count_b2) - count_b2) < 0.01:
                token_sum += round(count_b1) * 3 + round(count_b2)
        else:
            if 0 < count_b1 <= 100 and 0 < count_b2 <= 100 and abs(round(count_b1)-count_b1) < 0.01 and abs(round(count_b2)-count_b2) < 0.01:
                token_sum += round(count_b1)*3+round(count_b2)
        i+=4
    return token_sum

print(f"Part 1: {(calc_token_sum(machines))}")
print(f"Part 2: {(calc_token_sum(machines, part2=True))}")