#里井瑠海奈
import time
import matplotlib.pyplot as plt
import random as ra
import sys

sys.setrecursionlimit(1000000)

def quick(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left, right, same = [], [], 0

    for i in data:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            same += 1

    left = quick(left)
    right = quick(right)
    return left + [pivot] * same + right


result = []
x = list(range(0, 10000, 50))
for i in x:
    data = ra.sample(range(10000), i)
    start = time.perf_counter()
    quick(data)
    end = time.perf_counter()
    result.append(end - start)


fig = plt.figure()
plt.plot(x, result)
plt.draw()
plt.show()
