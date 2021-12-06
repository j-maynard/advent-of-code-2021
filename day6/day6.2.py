#!/usr/bin/python3
# Read the file in to an array
input = []
f = open("input.txt", "r")
i = f.readline()
input = i.split(',')

days = 256

def test(days, input):
    for d in range(0, days):
        for i in range(0,len(input)):
            if input[i] == 0:
                input[i] = 6
                input.append(8)
            else:
                input[i] = int(input[i]) - 1

def pop_cycle(input):
    cycle = [0]*9
    for i in input:
        cycle[int(i)] =+ cycle[int(i)] + 1
    return cycle

def tick(cycle):
    fish_to_spawn = cycle[0]
    cycle[7] = cycle[7] + cycle[0]
    for i in range(0, 8):
        cycle[i] = cycle[i+1]
    cycle[8] = fish_to_spawn

cycle = pop_cycle(input)

for d in range(0, days):
    tick(cycle)

total_fish = 0
for f in cycle:
    total_fish = total_fish + f

print(total_fish)