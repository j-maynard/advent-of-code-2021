#!/usr/bin/pyton3

previous_depth = 0
count = 0
f = open("input.txt", "r")
f.readline()
for l in f:
    if int(l) > previous_depth:
        count = count + 1 
    previous_depth = int(l)

print(f"Depth increases {count} times")
