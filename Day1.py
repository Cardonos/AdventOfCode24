import numpy as np

#Part1
data = np.loadtxt("Inputs/Day1.txt").transpose()
data.sort()
i = 0
sum = 0
while i < len(data[1]):
    sum += abs(data[0][i]-data[1][i])
    i += 1
print(sum)

#Part2
sim_score=0
for j in data[0]:
    count = np.where(data[1] == int(j))
    sim_score += j * len(count[0])
print(sim_score)
