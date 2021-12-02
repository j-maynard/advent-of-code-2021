#!/usr/bin/python3

depth = 0
forward = 0

f = open("input.txt", "r")
for l in f:
    cmd, val = l.split(' ')
    if cmd == "forward":
        forward = forward + int(val)
    elif cmd == "down":
        depth = depth + int(val)
    elif cmd == "up":
        depth = depth - int(val)

print(f"Final depth = {depth}, forward position = {forward}")
distance = depth * forward
print(f"distance = {distance}")
