#!/usr/bin/python3
with open('input.txt', 'r') as f: data = f.read()
inputs = [int(n) for n in data.split(',')]

max_val = max(inputs)

fuel_used = [0] * max_val
for i in range(0, max_val):
    total_fuel = 0
    for s in inputs:
        total_fuel = total_fuel + abs(s - i)
    fuel_used[i] = total_fuel

min_value = min(fuel_used)
min_index = fuel_used.index(min_value)
print(f"Min fuel used at position {min_index} total fuel used: {fuel_used[min_index]}")