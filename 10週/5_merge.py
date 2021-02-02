#里井瑠海奈
import matplotlib.pyplot as plt
import random as ra
from memory_profiler import  memory_usage
import sys

sys.setrecursionlimit(1000000)

def merge(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = merge(data[:mid])
    right = merge(data[mid:])
    return merge_sub(left, right)

#こちらはmergeから呼び出される関数
def merge_sub(left, right):
    result = []
    i, j = 0, 0

    while (i < len(left)) and (j < len(right)):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i < len(left):
        result.extend(left[i:])
    if j < len(right):
        result.extend(right[j:])
    return result

if __name__ == '__main__':
    result = []
    x = list(range(0, 2000, 100))

    for i in x:
        data = ra.sample(range(10000), i)
        men_usage = memory_usage((merge, (data,)))
        result.append(men_usage[0])
        print(i)

    fig = plt.figure()
    plt.plot(x, result)
    plt.draw()
    plt.show()
