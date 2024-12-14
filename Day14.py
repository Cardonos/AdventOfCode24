import numpy as np
import statistics

data = open("Inputs/Day14.txt").read().strip().split("\n")

def move(coordinates, room, speed, seconds):
    height, width = room
    x, y = coordinates
    x_speed,y_speed = speed
    x = (x + x_speed*seconds)%width
    y = (y + y_speed*seconds)%height
    return [x, y]

def safety_factor(room, size):
    height, width = size
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    i = 0
    while i < height/2-1:
        j = 0
        while j < width/2-1:
            q1 += room[i][j]
            j+=1
        i += 1
    i = 0
    while i < height / 2 - 1:
        j = round(width/2)+1
        while j < width:
            q2 += room[i][j]
            j += 1
        i += 1
    i = round(height/2)
    while i < height:
        j = 0
        while j < width / 2 - 1:
            q3 += room[i][j]
            j += 1
        i += 1
    i = round(height / 2)
    while i < height:
        j = round(width / 2)
        while j < width:
            q4 += room[i][j]
            j += 1
        i += 1
    return q1*q2*q3*q4


def check_for_tree():
    t = 0
    max_x = 0
    max_y = 0
    bathroom = np.zeros([103,101])
    while True:
        for robot in robots:
            x_coord = int(robot[0].split(",")[0][2:])
            y_coord = int(robot[0].split(",")[1])
            v_x = int(robot[1].split(",")[0][2:])
            v_y = int(robot[1].split(",")[1])
            end_x,end_y = move([x_coord,y_coord],np.shape(bathroom),[v_x,v_y],t)
            bathroom[end_y][end_x] += 1
            '''
            i = 0
            while i < 103:
                j = 0
                while j < 101:
                    if sum(sum(bathroom[i:i+10, j:j+5])) > 15:
                        print("yep", t)
                        print(bathroom[i:i+10, j:j+5])
                    j += 5
                i += 5
            '''
        a = statistics.stdev(np.sum(bathroom,0))
        if a > max_x:
            max_x = a
        b = statistics.stdev(np.sum(bathroom,1))
        if b > max_y:
            max_y = b
        if a >= 7.4663:
            if b >= 6.83474:
                print(f"Part 2: {t}")
                return
        bathroom = np.zeros([103,101])

        t+=1
    return

bathroom = np.zeros([103,101])

robots = []
for robot in data:
    robots.append(robot.split())
#Part1
for robot in robots:
    x_coord = int(robot[0].split(",")[0][2:])
    y_coord = int(robot[0].split(",")[1])
    v_x = int(robot[1].split(",")[0][2:])
    v_y = int(robot[1].split(",")[1])
    end_x, end_y = move([x_coord, y_coord], np.shape(bathroom), [v_x, v_y], 100)
    bathroom[end_y][end_x] += 1

print(f"Part 1: {safety_factor(bathroom, np.shape(bathroom))}")

check_for_tree()