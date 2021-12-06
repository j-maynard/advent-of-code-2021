#!/usr/bin/python3
# Read the file in to an array
input = []
f = open("input.txt", "r")
for l in f:
    input.append(l)

def find_search_bit(position, input_list):
    v = ""
    for i in input_list:
        v = v + i[position]
    
    if v.count('1') == v.count('0'):
        return 1
    elif v.count('1') > v.count('0'):
        return 1
    else:
        return 0

def filter_list(position, filter, input_list):
    out_list = []
    if position > len(input_list[0]):
        print("Error: search position is longer than input string length")
    for i in input_list:
        if str(i[position]) == str(filter):
            out_list.append(i)
    return out_list

o2_list = input.copy()
co2_list = input.copy()

for i in range(0, len(input[0])-1):
    o2_search_bit = find_search_bit(i, o2_list)
    o2_list = filter_list(i, o2_search_bit, o2_list)
    if len(o2_list) < 2:
        break

print(f"O2 List = {o2_list}")

for i in range(0, len(input[0])-1):
    co2_search_bit = find_search_bit(i, co2_list)
    if co2_search_bit == 1:
        co2_search_bit = 0
    else:
        co2_search_bit = 1
    co2_list = filter_list(i, co2_search_bit, co2_list)
    if len(co2_list) < 2:
        break

print(f"CO2 List = {o2_list}")

print(f"result = {int(o2_list[0],2) * int(co2_list[0],2)}")
