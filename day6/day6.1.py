#!/usr/bin/python3
# Read the file in to an array
input = []
f = open("test_input.txt", "r")
i = f.readline()
input = i.split(',')

days = 80

#print(f"Initial state: {input}")
for d in range(0, days):
    for i in range(0,len(input)):
        if input[i] == 0:
            input[i] = 6
            input.append(8)
        else:
            input[i] = int(input[i]) - 1
    #print(f"Day {d}")

print(input)
print(f"No fish = {len(input)}")
