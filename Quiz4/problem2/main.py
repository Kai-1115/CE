import random
from collections import Counter
from itertools import permutations

cards = [1, 2, 3, 4]
naive_count = Counter()
fy_count = Counter()

def naive_shuffle(cards):
    arr = cards[:]
    for i in range(len(arr)):
        n = random.randint(0, len(arr)-1)
        arr[i], arr[n] = arr[n], arr[i]
    return tuple(arr)

def fisher_yates(cards):
    arr = cards[:]
    for i in range(len(arr)-1, 0, -1):
        n = random.randint(0, i)
        arr[i], arr[n] = arr[n], arr[i]
    return tuple(arr)

for _ in range(1000000):
    naive_count[naive_shuffle(cards)] += 1
    fy_count[fisher_yates(cards)] += 1

print("Naive shuffle:")

for k, v in naive_count.items():
    print(f"{list(k)}: {v}")

print("\nFisher-Yates shuffle:")
for k, v in fy_count.items():
    print(f"{list(k)}: {v}")

