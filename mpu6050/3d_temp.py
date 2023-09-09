from matplotlib import pyplot as plt  # 用来绘制图形
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

'''
X1 = X2 = np.arange(-5, 15, 3)
X1, X2 = np.meshgrid(X1, X2)
Z = 1 / 2 * X1 ** 2
'''
X1 = [0, 1]
X2 = [0, 2]
Z = [0, 3]
# 创建绘制实时损失的动态窗口

plt.ion()
for i in range(30000):
    plt.clf()  # 清除之前画的图
    fig = plt.gcf()  # 获取当前图
    ax = fig.gca(projection='3d')  # 获取当前轴
    ax.set_xlim3d(-5, 5)
    ax.set_ylim3d(-5, 5)
    ax.set_zlim3d(-5, 5)
    ax.plot(X1, X2, Z)
    plt.pause(0.001)  # 暂停一段时间，不然画的太快会卡住显示不出来
    plt.ioff()  # 关闭画图窗口Z

    X1[1] = (X1[1]+1) % 4
    X2[1] = (X2[1]+1) % 4
    Z[1] = (Z[1]+1) % 4

# 加这个的目的是绘制完后不让窗口关闭
plt.show()
