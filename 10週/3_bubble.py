#里井瑠海奈
import matplotlib.pyplot as plt
import random as ra
from memory_profiler import  memory_usage

def bubble(data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

if __name__ == '__main__':
    result = []
    x = list(range(0, 2000, 100))

    for i in x:
        data = ra.sample(range(10000), i)
        men_usage = memory_usage((bubble, (data,)))
        result.append(men_usage[0])
        print(i)

    fig = plt.figure()
    plt.plot(x, result)
    plt.draw()
    plt.show()
