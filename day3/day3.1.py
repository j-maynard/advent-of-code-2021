#!/usr/bin/python3
# Read the file in to an array
input = []
f = open("input.txt", "r")
for l in f:
    input.append(l)

positions = []
for i in range(0, len(input[0])):
    vert = ""
    for x in input:
        vert = vert + x[i]
    positions.append(vert)

gamma = ""
epsilon = ""
for x in range(0, len(input[0])-1):
    i = positions[x].count('1')
    o = positions[x].count('0')
    if i > o:
        gamma = gamma + "1"
        epsilon = epsilon + "0"
    else:
        gamma = gamma + "0"
        epsilon = epsilon + "1"

print(f"Result = {int(gamma, 2) * int(epsilon, 2)}")