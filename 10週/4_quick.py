#里井瑠海奈
import matplotlib.pyplot as plt
import random as ra
from memory_profiler import  memory_usage
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

if __name__ == '__main__':
    result = []
    x = list(range(0, 2000, 100))

    for i in x:
        data = ra.sample(range(10000), i)
        men_usage = memory_usage((quick, (data,)))
        result.append(men_usage[0])
        print(i)

    fig = plt.figure()
    plt.plot(x, result)
    plt.draw()
    plt.show()
