#里井瑠海奈
import time
import matplotlib.pyplot as plt
import random as ra


def bubble(data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

result = []
x = list(range(0, 1000, 10))
for i in x:
    data = ra.sample(range(10000), i)
    start = time.perf_counter()
    bubble(data)
    end = time.perf_counter()
    result.append(end - start)

fig = plt.figure()
plt.plot(x, result)
plt.draw()
plt.show()
