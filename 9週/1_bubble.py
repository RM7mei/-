#里井瑠海奈
import matplotlib.pyplot as plt

data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
x = list(range(1, len(data)+1))

def bubble(data):
    global x
    fig = plt.figure()
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                b = plt.bar(x, data)
                b[j+1].set_color('r') # 内側のfor文で確定した値の棒グラフを赤くする
                plt.draw()
                plt.pause(0.01) # グラフを描画した後に0.01秒停止する
                fig.clear()


fig = plt.figure()
b = plt.bar(x, data)
plt.draw()
plt.show()

bubble(data)

b = plt.bar(x, data)
plt.draw()
plt.show()

print(data)
