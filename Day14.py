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
    q1 = sum(sum(room[0:round(height/2)-1, 0:round(width/2)]))
    q2 = sum(sum(room[0:round(height/2)-1,round(width/2)+1::]))
    q3 = sum(sum(room[round(height/2)::, 0:round(width/2)-1]))
    q4 = sum(sum(room[round(height/2)::,round(width/2)+1::]))
    return q1*q2*q3*q4


def check_for_tree():
    t = 0
    max_x = 4
    max_y = 4
    bathroom = np.zeros([103,101])
    while True:
        for robot in robots:
            x_coord = int(robot[0].split(",")[0][2:])
            y_coord = int(robot[0].split(",")[1])
            v_x = int(robot[1].split(",")[0][2:])
            v_y = int(robot[1].split(",")[1])
            end_x,end_y = move([x_coord,y_coord],np.shape(bathroom),[v_x,v_y],t)
            bathroom[end_y][end_x] += 1
        #Check for the standard deviation of sum in x-direction and y-direction
        #the picture will be unusually ordered, so when both standard deviations are at their maximum it is very
        #likely it is the solution
        a = statistics.stdev(np.sum(bathroom,0))
        if a > max_x:
            max_x = a
        b = statistics.stdev(np.sum(bathroom,1))
        if b > max_y:
            max_y = b
        if a >= max_x:
            if b >= max_y:
                print(f"Part 2: {t}")
                return
        bathroom = np.zeros([103,101])
        t+=1

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

#Part2
check_for_tree()