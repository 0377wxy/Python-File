
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

# plt.style.use('Solarize_Light2')
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams["figure.figsize"] = (8,5)

x_min = 0.0
x_max = 30.0

mean = 9.0 
std = 2.0

# 生成数据的 x-坐标
x1 = np.linspace(x_min, x_max, 100)
# 计算数据的 y-坐标
y1 = scipy.stats.norm.pdf(x1, mean, std)

print(x1)
print(y1)

plt.figure(figsize=(8, 5), facecolor='w', edgecolor='k') 
plt.plot(x1, y1, color='black')
#plt.fill_between(x1, y1, color='#89bedc', alpha=1.0);
plt.show()
