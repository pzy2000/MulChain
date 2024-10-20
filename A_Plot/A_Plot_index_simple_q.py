import matplotlib.pyplot as plt
from matplotlib import rcParams

config = {
    "font.family": 'serif',
    "font.size": 20,
    "mathtext.fontset": 'stix',
    "font.serif": ['Times New Roman'],
}
rcParams.update(config)
# 实验数据
x = [16, 32, 64, 128, 256, 512, 1024]
data = [75.3876, 88.8538, 147.1636, 286.0087, 584.5755, 1136.2391, 2356.1634]

On_Chain_data = [19.1831, 37.7805, 75.1768, 149.4479, 296.7697, 594.6269, 265.9659]
vChain_data = [19.3730, 37.9705, 75.3668, 149.6378, 296.9596, 594.8168, 3090]

index_size = [0.0144, 0.0258, 0.0861, 0.3104, 1.1746, 4.6510, 18.9673]
On_Chain_index_size = [0.008, 0.02, 0.08, 0.26, 0.88, 3.2, 12.9]
vChain_index_size = [1.0607, 2.9987, 4.3441, 8.9967, 10.9882, 20.6771, 30.5647]

# 动态计算每个柱状的宽度
widths_bar = [value / 8 for value in x]
# print("width", widths)

# 创建图形和子图
fig, axs = plt.subplots(1, 4, figsize=(24, 4), dpi=360)

# 第一个子图：CPU Time vs Block Number
bar1 = [value - w for value, w in zip(x, widths_bar)]  # 左侧的柱状位置
bar2 = [value for value, w in zip(x, widths_bar)]  # mid的柱状位置
bar3 = [value + w for value, w in zip(x, widths_bar)]  # 右侧的柱状位置

from matplotlib.patches import Rectangle

# 使用 Rectangle 来实现 hatch 的自定义颜色
max_i = -1  # 初始化为 -1，确保在循环开始前有一个合理的初始值

for i, (pos, height) in enumerate(zip(bar1, On_Chain_data)):
    max_i = i  # 在每次迭代中更新 max_i 为当前的 i
    # 这里是你在循环中要执行的其他代码

# 在循环结束后，max_i 就是 i 的最大值
print("最大值 i:", max_i)

for i, (pos, height) in enumerate(zip(bar1, On_Chain_data)):
    rect1 = Rectangle(
        (pos - widths_bar[i] / 2, 0),  # 矩形左下角的坐标
        widths_bar[i],  # 矩形的宽度
        height,  # 矩形的高度
        linewidth=1,
        edgecolor='#C1A4CD',
        facecolor='white',  # 设置背景色为白色
        hatch='XX'
    ) if i != max_i else Rectangle(
        (pos - widths_bar[i] / 2, 0),  # 矩形左下角的坐标
        widths_bar[i],  # 矩形的宽度
        height,  # 矩形的高度
        linewidth=1,
        edgecolor='#C1A4CD',
        facecolor='white',  # 设置背景色为白色
        hatch='XX', label='oChain$_o$'
    )
    axs[0].add_patch(rect1)
    rect = Rectangle(
        (pos - widths_bar[i] / 2, 0),  # 矩形左下角的坐标
        widths_bar[i],  # 矩形的宽度
        height,  # 矩形的高度
        linewidth=1,
        edgecolor='black',
        facecolor='none'
    )
    axs[0].add_patch(rect)
# axs[0].add_patch(Patch(edgecolor='black', hatch='*', color='#C1A4CD'))
axs[0].bar(bar2, data, color=(14 / 255, 157 / 255, 205 / 255), width=widths_bar, hatch=r'\/', edgecolor='black',
           label='oChain')
# axs[0].bar(bar3, vChain_data, color='green', width=widths_bar, hatch='x', edgecolor='black', label='vChain+')

# 设置第一个子图的坐标轴
axs[0].set_xlabel('Block Number', fontsize=20)
axs[0].set_ylabel('CPU time (s)', fontsize=20)
axs[0].set_xscale('log', base=2)  # 设置x轴为对数制度，底数为2
axs[0].set_yscale('log')  # 设置y轴为对数制度
axs[0].set_xticks(x)  # 设置X轴制点
axs[0].set_yticks([10 ** 0, 10 ** 1, 10 ** 2, 10 ** 3], ['$10^0$', '$10^1$', '$10^2$', '$10^3$'])
axs[0].set_xticklabels(x, fontsize=20)
axs[0].set_yticklabels(['$10^0$', '$10^1$', '$10^2$', '$10^3$'], fontsize=20)

axs[0].set_title('(a) BTC', fontsize=20)
axs[0].legend(fontsize=16)
axs[0].grid(axis='y', linestyle='--', linewidth=0.7)

for i, (pos, height) in enumerate(zip(bar1, On_Chain_data)):
    rect1 = Rectangle(
        (pos - widths_bar[i] / 2, 0),  # 矩形左下角的坐标
        widths_bar[i],  # 矩形的宽度
        height,  # 矩形的高度
        linewidth=1,
        edgecolor='#C1A4CD',
        facecolor='white',  # 设置背景色为白色
        hatch='XX'
    ) if i != max_i else Rectangle(
        (pos - widths_bar[i] / 2, 0),  # 矩形左下角的坐标
        widths_bar[i],  # 矩形的宽度
        height,  # 矩形的高度
        linewidth=1,
        edgecolor='#C1A4CD',
        facecolor='white',  # 设置背景色为白色
        hatch='XX', label='oChain$_o$'
    )
    axs[1].add_patch(rect1)
    rect = Rectangle(
        (pos - widths_bar[i] / 2, 0),  # 矩形左下角的坐标
        widths_bar[i],  # 矩形的宽度
        height,  # 矩形的高度
        linewidth=1,
        edgecolor='black',
        facecolor='none'
    )
    axs[1].add_patch(rect)
# axs[1].add_patch(Patch(edgecolor='black', hatch='*', color='#C1A4CD'))
axs[1].bar(bar2, data, color=(14 / 255, 157 / 255, 205 / 255), width=widths_bar, hatch=r'\/', edgecolor='black',
           label='oChain')
# axs[1].bar(bar3, vChain_data, color='green', width=widths_bar, hatch='x', edgecolor='black', label='vChain+')

# 设置第2个子图的坐标轴
axs[1].set_xlabel('Block Number', fontsize=20)
axs[1].set_ylabel('CPU time (s)', fontsize=20)
axs[1].set_xscale('log', base=2)  # 设置x轴为对数制度，底数为2
axs[1].set_yscale('log')  # 设置y轴为对数制度
axs[1].set_xticks(x)  # 设置X轴制点
axs[1].set_yticks([10 ** 0, 10 ** 1, 10 ** 2, 10 ** 3], ['$10^0$', '$10^1$', '$10^2$', '$10^3$'])
axs[1].set_xticklabels(x, fontsize=20)
axs[1].set_yticklabels(['$10^0$', '$10^1$', '$10^2$', '$10^3$'], fontsize=20)

axs[1].set_title('(b) ETH', fontsize=20)
axs[1].legend(fontsize=16)
axs[1].grid(axis='y', linestyle='--', linewidth=0.7)

# 第3个子图：Index Size vs Block Number
bar6 = [value - w for value, w in zip(x, widths_bar)]  # 左侧的柱状位置
bar4 = [value for value, w in zip(x, widths_bar)]  # 左侧的柱状位置
bar5 = [value + w for value, w in zip(x, widths_bar)]  # 右侧的柱状位置
axs[2].bar(bar4, index_size, color=(14 / 255, 157 / 255, 205 / 255), width=widths_bar, hatch=r'\/', edgecolor='black',
           label='oChain')
# axs[2].bar(bar5, vChain_index_size, color='green', width=widths_bar, hatch='x', edgecolor='black', label='vChain+')

# 设置第二个子图的坐标轴
axs[2].set_xlabel('Block Number', fontsize=20)
axs[2].set_ylabel('Index size (MB)', fontsize=20)
axs[2].set_xscale('log', base=2)  # 设置x轴为对数制度，底数为2
axs[2].set_yscale('log')  # 设置y轴为对数制度
axs[2].set_xticks(x)  # 设置X轴制点
axs[2].set_yticks([10 ** -3, 10 ** -2, 10 ** -1, 10 ** 0],
                  ['$10^{-3}$', '$10^{-2}$', '$10^{-1}$', '$10^{0}$'])
axs[2].set_xticklabels(x, fontsize=20)
axs[2].set_yticklabels(['$10^{-3}$', '$10^{-2}$', '$10^{-1}$', '$10^{0}$'], fontsize=20)

axs[2].set_title('(c) BTC', fontsize=20)
axs[2].legend(fontsize=16)
axs[2].grid(axis='y', linestyle='--', linewidth=0.7)

# 第3个子图：Index Size vs Block Number
bar9 = [value - w for value, w in zip(x, widths_bar)]  # 左侧的柱状位置
bar7 = [value for value, w in zip(x, widths_bar)]  # 左侧的柱状位置
bar8 = [value + w for value, w in zip(x, widths_bar)]  # 右侧的柱状位置
axs[3].bar(bar7, index_size, color=(14 / 255, 157 / 255, 205 / 255), width=widths_bar, hatch=r'\/', edgecolor='black',
           label='oChain')
# axs[3].bar(bar5, vChain_index_size, color='green', width=widths_bar, hatch='x', edgecolor='black', label='vChain+')

# 设置第二个子图的坐标轴
axs[3].set_xlabel('Block Number', fontsize=20)
axs[3].set_ylabel('Index size (MB)', fontsize=20)
axs[3].set_xscale('log', base=2)  # 设置x轴为对数制度，底数为2
axs[3].set_yscale('log')  # 设置y轴为对数制度
axs[3].set_xticks(x)  # 设置X轴制点
axs[3].set_yticks([10 ** -3, 10 ** -2, 10 ** -1, 10 ** 0],
                  ['$10^{-3}$', '$10^{-2}$', '$10^{-1}$', '$10^{0}$'])
axs[3].set_xticklabels(x, fontsize=20)
axs[3].set_yticklabels(['$10^{-3}$', '$10^{-2}$', '$10^{-1}$', '$10^{0}$'], fontsize=20)

axs[3].set_title('(d) ETH', fontsize=20)
axs[3].legend(fontsize=16)
axs[3].grid(axis='y', linestyle='--', linewidth=0.7)

# 调整子图布局
plt.tight_layout()

# 保存图表
plt.savefig('../Figures/SimpleQ_all.png', dpi=360)

# 显示图表
plt.show()
