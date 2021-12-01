#!/usr/bin/pyton3
def create_m_window(size, index, measurements):
    window = 0
    for i in range(size):
        if index + i >= len(measurements):
            break
        window = window + measurements[i + index]
    return window

f = open("input.txt", "r")
measurements = []
combined_measurements = []
for l in f:
    measurements.append(int(l))

# create measurement windows
window_size = 3
for i in range(len(measurements)):
    combined_measurements.append(create_m_window(window_size, i, measurements))

count = 0
previous_depth = 0
combined_measurements.pop(0)

for m in combined_measurements:
    if m > previous_depth:
        count = count + 1
    previous_depth = m

print(f"Depth increases {count} times")
