#!/usr/bin/python3
# Read the file in to an array
from threading import Thread

input = []
f = open("test_input.txt", "r")
i = f.readline()
input = i.split(',')

def thread_function(fish_pool, days):
    for d in range(0, days):
        for i in range(0,len(fish_pool)):
            if fish_pool[i] == 0:
                fish_pool[i] = 6
                fish_pool.append(8)
            else:
                fish_pool[i] = int(fish_pool[i]) - 1

days = 10
times = 8
all_fish = input.copy()
for x in range(0,10):
    threads = []
    results = []
    for f in range(0, len(all_fish)):
        fish_pool = [all_fish[f]]
        results.append(fish_pool)
        t = Thread(target=thread_function, args=(fish_pool, days))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    for r in results:
        all_fish = all_fish + r

print(f"No fish = {len(all_fish)}")