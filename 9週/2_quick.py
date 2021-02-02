#里井瑠海奈
import matplotlib.pyplot as plt
import networkx as nx

data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

def quick_sort(data):
    global G
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

    G.add_edge(str(data), str(left))

    left = quick_sort(left)

    G.add_edge(str(data), str(right))

    right = quick_sort(right)
    return left + [pivot] * same + right

G = nx.DiGraph()

print(quick_sort(data))

nx.draw_networkx(G)
plt.show()
