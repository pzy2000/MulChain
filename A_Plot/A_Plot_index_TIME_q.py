import matplotlib.pyplot as plt

# 实验数据
x = [32, 64, 128, 256, 512, 1024, 2048]
data = [5.3793, 5.2412 + 5.3793, 10.7096 + 5.2412 + 5.3793, 21.1219 + 10.7096 + 5.2412 + 5.3793,
        42.6031 + 21.1219 + 10.7096 + 5.2412 + 5.3793, 85.8600 + 42.6031 + 21.1219 + 10.7096 + 5.2412 + 5.3793,
        173.1463 + 85.8600 + 42.6031 + 21.1219 + 10.7096 + 5.2412 + 5.3793]
# On_Chain_data = [24.6685, 48.9040-24.6685, 97.3067-48.9040-24.6685, 193.4260-97.3067-48.9040-24.6685,
#                  387.9510-193.4260-97.3067-48.9040-24.6685, 861.6666-387.9510-193.4260-97.3067-48.9040-24.6685,
#                  1837.8888-819.6666-387.9510-193.4260-97.3067-48.9040-24.6685]
On_Chain_data = [5.1359, 5.2412 + 5.1359, 10.7096 + 5.2412 + 5.1359, 21.1219 + 10.7096 + 5.2412 + 5.1359,
                 42.6031 + 21.1219 + 10.7096 + 5.2412 + 5.1359, 85.8600 + 42.6031 + 21.1219 + 10.7096 + 5.2412 + 5.1359,
                 173.1463 + 85.8600 + 42.6031 + 21.1219 + 10.7096 + 5.2412 + 5.1359]
# vChain_data = [86, 130, 250, 320, 1060, 2026, 3090]

index_size = [0.00251687, 0.00270743, 0.00595963, 0.01376983, 0.03518055, 0.09485251, 0.29619724]
# On_Chain_index_size = [0.00251687, 0.02, 0.08, 0.26, 0.88, 3.2, 12.9]
# vChain_index_size = [1.0607, 2.9987, 4.3441, 8.9967, 10.9882, 20.6771, 30.5647]

# 动态计算每个柱状的宽度
widths_bar = [value / 8 for value in x]
# print("width", widths)

# 创建图形和子图
fig, axs = plt.subplots(1, 2, figsize=(16, 6), dpi=360)

# 第一个子图：CPU Time vs Block Number
bar1 = [value - w for value, w in zip(x, widths_bar)]  # 左侧的柱状位置
bar2 = [value for value, w in zip(x, widths_bar)]  # mid的柱状位置
bar3 = [value + w for value, w in zip(x, widths_bar)]  # 右侧的柱状位置
from matplotlib.patches import Patch

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
        edgecolor='purple',
        facecolor='white',  # 设置背景色为白色
        hatch='XX'
    ) if i != max_i else Rectangle(
        (pos - widths_bar[i] / 2, 0),  # 矩形左下角的坐标
        widths_bar[i],  # 矩形的宽度
        height,  # 矩形的高度
        linewidth=1,
        edgecolor='purple',
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
# axs[0].add_patch(Patch(edgecolor='black', hatch='*', color='purple'))
axs[0].bar(bar2, data, color='blue', width=widths_bar, hatch=r'\/', edgecolor='black', label='oChain')
# axs[0].bar(bar3, vChain_data, color='green', width=widths_bar, hatch='x', edgecolor='black', label='vChain+')

# 设置第一个子图的坐标轴
axs[0].set_xlabel('Block Number', fontsize=16)
axs[0].set_ylabel('CPU time (s)', fontsize=16)
axs[0].set_xscale('log', base=2)  # 设置x轴为对数制度，底数为2
axs[0].set_yscale('log')  # 设置y轴为对数制度
axs[0].set_xticks(x)  # 设置X轴制点
axs[0].set_yticks([10 ** 0, 10 ** 1, 10 ** 2, 10 ** 3, 10 ** 4], ['$10^0$', '$10^1$', '$10^2$', '$10^3$', '$10^4$'])
axs[0].set_title('CPU Time vs Block Number', fontsize=16)
axs[0].legend(fontsize=12)
axs[0].grid(axis='y', linestyle='--', linewidth=0.7)

# 第二个子图：Index Size vs Block Number
bar6 = [value - w for value, w in zip(x, widths_bar)]  # 左侧的柱状位置
bar4 = [value for value, w in zip(x, widths_bar)]  # 左侧的柱状位置
bar5 = [value + w for value, w in zip(x, widths_bar)]  # 右侧的柱状位置
# axs[1].bar(bar6, On_Chain_index_size, color='white', width=widths_bar, hatch='*',
#            edgecolor='black', label='oChain$_o$')
for i, (pos, height) in enumerate(zip(bar6, On_Chain_index_size)):
    rect1 = Rectangle(
        (pos - widths_bar[i] / 2, 0),  # 矩形左下角的坐标
        widths_bar[i],  # 矩形的宽度
        height,  # 矩形的高度
        linewidth=1,
        edgecolor='purple',
        facecolor='white',  # 设置背景色为白色
        hatch='XX'
    ) if i != max_i else Rectangle(
        (pos - widths_bar[i] / 2, 0),  # 矩形左下角的坐标
        widths_bar[i],  # 矩形的宽度
        height,  # 矩形的高度
        linewidth=1,
        edgecolor='purple',
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
axs[1].bar(bar4, index_size, color='blue', width=widths_bar, hatch=r'\/', edgecolor='black', label='oChain')
# axs[1].bar(bar5, vChain_index_size, color='green', width=widths_bar, hatch='x', edgecolor='black', label='vChain+')

# 设置第二个子图的坐标轴
axs[1].set_xlabel('Block Number', fontsize=16)
axs[1].set_ylabel('Index size (MB)', fontsize=16)
axs[1].set_xscale('log', base=2)  # 设置x轴为对数制度，底数为2
axs[1].set_yscale('log')  # 设置y轴为对数制度
axs[1].set_xticks(x)  # 设置X轴制点
axs[1].set_yticks([10 ** -2, 10 ** -1, 10 ** 0, 10 ** 1, 10 ** 2],
                  ['$10^{-2}$', '$10^{-1}$', '$10^0$', '$10^1$', '$10^2$'])
axs[1].set_title('Index Size vs Block Number', fontsize=16)
axs[1].legend(fontsize=12)
axs[1].grid(axis='y', linestyle='--', linewidth=0.7)

# 调整子图布局
plt.tight_layout()

# 保存图表
plt.savefig('Index Cost.png', dpi=360)

# 显示图表
plt.show()
