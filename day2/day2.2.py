#!/usr/bin/python3

aim = 0
depth = 0
forward = 0

f = open("input.txt", "r")
for l in f:
    cmd, val = l.split(' ')
    if cmd == "forward":
        forward = forward + int(val)
        depth = depth + (aim * int(val))
    elif cmd == "down":
        aim = aim + int(val)
    elif cmd == "up":
        aim = aim - int(val)

print(f"Final depth = {depth}, forward position = {forward}")
distance = depth * forward
print(f"distance = {distance}")
