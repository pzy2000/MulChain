import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

config = {
    "font.family": 'serif',
    "font.size": 24,
    "mathtext.fontset": 'stix',
    "font.serif": ['Times New Roman'],
}
rcParams.update(config)

x = [16, 32, 64, 128, 256, 512, 1024]
Mulchain_v_CPU_Time_BTC = [2.7086, 2.6448, 2.5843, 2.5241, 2.4866, 2.4757, 2.4820]
Mulchain_o_CPU_Time_BTC = [2.5136, 2.4611, 2.4142, 2.3592, 2.3248, 2.3137, 2.3207]
Mulchain_v_CPU_Time_ETH = [2.6555, 2.5892, 2.5309, 2.5048, 2.4910, 2.5169, 2.5323]
Mulchain_o_CPU_Time_ETH = [2.4691, 2.4073, 2.3610, 2.3394, 2.3284, 2.3557, 2.3712]

# 创建图形和子图
fig, axs = plt.subplots(1, 3, figsize=(18, 6), dpi=360)

# 第1个子图：CPU Time vs Number (Blocks)
axs[0].plot(x, Mulchain_o_CPU_Time_BTC, marker='o', linestyle='-', color='black',
            label='MulChain$_OB$', markerfacecolor='none', markersize=10, linewidth=3.0)
axs[0].plot(x, Mulchain_o_CPU_Time_ETH, marker='s', linestyle='-', color='#33FF57',
            label='MulChain$_OE$', markerfacecolor='none', markersize=10, linewidth=3.0)
axs[0].plot(x, Mulchain_v_CPU_Time_BTC, marker='^', linestyle='-', color='#8B4513',
            label='MulChain$_VB$', markerfacecolor='none', markersize=10, linewidth=3.0)
axs[0].plot(x, Mulchain_v_CPU_Time_ETH, marker='D', linestyle='-', color='blue',
            label='MulChain$_VE$', markerfacecolor='none', markersize=10, linewidth=3.0)

# 设置第一个子图的坐标轴
axs[0].set_xlabel('Number (Blocks)\n(a) Index Construction Cost', fontsize=28)
axs[0].set_ylabel('CPU time (s)', fontsize=28)
axs[0].set_xscale('log', base=2)  # 设置x轴为对数制度，底数为2
axs[0].set_xticks(x, ['$2^{4}$', '$2^{5}$', '$2^{6}$', '$2^{7}$', '$2^{8}$', '$2^{9}$', '$2^{10}$'])  # 设置X轴刻度
# axs[0].set_xticklabels(x, fontsize=20)

# axs[0].legend(fontsize=12, loc='upper center', bbox_to_anchor=(0.5, 1.25), ncol=2)
axs[0].grid(axis='x', linestyle='--', linewidth=1.2)
axs[0].grid(axis='y', linestyle='--', linewidth=1.2)

# 第2个子图：Latency vs Number (Blocks)
Mulchain_v_latency_BTC = [0.5215, 0.5381, 0.5483, 0.5484, 0.5460, 0.5469, 0.5412]
Mulchain_o_latency_BTC = [0.0263, 0.0247, 0.0245, 0.0243, 0.0244, 0.0242, 0.0243]

Mulchain_v_latency_ETH = [0.5214, 0.5375, 0.5500, 0.5494, 0.5474, 0.5472, 0.5403]
Mulchain_o_latency_ETH = [0.0250, 0.0249, 0.0249, 0.0247, 0.0245, 0.0241, 0.0241]

axs[1].plot(x, Mulchain_o_latency_BTC, marker='o', linestyle='-', color='black',
            label='MulChain$_OB$', markerfacecolor='none', markersize=10, linewidth=3.0)
axs[1].plot(x, Mulchain_o_latency_ETH, marker='s', linestyle='-', color='#33FF57',
            label='MulChain$_OE$', markerfacecolor='none', markersize=10, linewidth=3.0)
axs[1].plot(x, Mulchain_v_latency_BTC, marker='^', linestyle='-', color='#8B4513',
            label='MulChain$_VB$', markerfacecolor='none', markersize=10, linewidth=3.0)
axs[1].plot(x, Mulchain_v_latency_ETH, marker='D', linestyle='-', color='blue',
            label='MulChain$_VE$', markerfacecolor='none', markersize=10, linewidth=3.0)

axs[1].set_xlabel('Number (Blocks)\n(b) Latency', fontsize=28)
axs[1].set_ylabel('Latency (s)', fontsize=28)
axs[1].set_xscale('log', base=2)  # 设置x轴为对数制度，底数为2
axs[1].set_xticks(x, ['$2^{4}$', '$2^{5}$', '$2^{6}$', '$2^{7}$', '$2^{8}$', '$2^{9}$', '$2^{10}$'])  # 设置X轴刻度

# axs[1].set_xticklabels(x, fontsize=20)

# axs[1].legend(fontsize=12, loc='upper center', bbox_to_anchor=(0.5, 1.25), ncol=2)
axs[1].grid(axis='x', linestyle='--', linewidth=1.2)
axs[1].grid(axis='y', linestyle='--', linewidth=1.2)

# 子坐标系显示范围
axins = axs[1].inset_axes((0.21, 0.3, 0.35, 0.28))
axins.plot(x, Mulchain_o_latency_BTC, marker='o', linestyle='-', color='black',
           label='MulChain$_{OB}$', markerfacecolor='none', markersize=10, linewidth=3.0)
axins.plot(x, Mulchain_o_latency_ETH, marker='s', linestyle='-', color='#33FF57',
           label='MulChain$_{OE}$', markerfacecolor='none', markersize=10, linewidth=3.0)
axins.plot(x, Mulchain_v_latency_BTC, marker='^', linestyle='-', color='#8B4513',
           label='MulChain$_{VB}$', markerfacecolor='none', markersize=10, linewidth=3.0)
axins.plot(x, Mulchain_v_latency_ETH, marker='D', linestyle='-', color='blue',
           label='MulChain$_{VE}$', markerfacecolor='none', markersize=10, linewidth=3.0)
# axins.set_xscale('log', base=2)  # 设置x轴为对数尺度，底数为2
# axins.set_xticks(x)  # 设置X轴刻度
# axins.set_yscale('log')  # 设置y轴为对数尺度
zone_left = 0
zone_right = 2

# 坐标轴的扩展比例（根据实际数据调整）
x_ratio = 0.05  # x轴显示范围的扩展比例
y_ratio = 1.5  # y轴显示范围的扩展比例

# X轴的显示范围
xlim0 = x[zone_left] - (x[zone_right] - x[zone_left]) * x_ratio
xlim1 = x[zone_right] + (x[zone_right] - x[zone_left]) * x_ratio

# Y轴的显示范围
y = np.hstack((Mulchain_v_latency_BTC[zone_left:zone_right],
               Mulchain_v_latency_ETH[zone_left:zone_right]))
ylim0 = np.min(y) - (np.max(y) - np.min(y)) * y_ratio
ylim1 = np.max(y) + (np.max(y) - np.min(y)) * y_ratio

# 调整子坐标系的显示范围
axins.set_xlim(xlim0, xlim1)
axins.set_ylim(ylim0, ylim1)
mark_inset(axs[1], axins, loc1=3, loc2=1, fc="none", ec='k', lw=0.5)

# 第3个子图：VO Size vs Number (Blocks)
Mulchain_v_VO_BTC = [76.7972, 76.7978, 76.7981, 76.7982, 76.7983, 76.8079, 76.8127]
Mulchain_v_VO_ETH = [98.2340, 98.2346, 98.2349, 98.2351, 98.2351, 98.2447, 98.2495]
axs[2].plot(x, Mulchain_v_VO_BTC, marker='^', linestyle='-', color='#8B4513',
            label='MulChain$_VB$', markerfacecolor='none', markersize=10, linewidth=3.0)
axs[2].plot(x, Mulchain_v_VO_ETH, marker='D', linestyle='-', color='blue',
            label='MulChain$_VE$', markerfacecolor='none', markersize=10, linewidth=3.0)

# 设置第3个子图的坐标轴
axs[2].set_xlabel('Number (Blocks)\n(c) VO Size', fontsize=28)
axs[2].set_ylabel('VO Size (KB)', fontsize=28)
axs[2].set_xscale('log', base=2)  # 设置x轴为对数制度，底数为2
axs[2].set_xticks(x, ['$2^{4}$', '$2^{5}$', '$2^{6}$', '$2^{7}$', '$2^{8}$', '$2^{9}$', '$2^{10}$'])  # 设置X轴刻度
axs[2].grid(axis='x', linestyle='--', linewidth=1.2)
axs[2].grid(axis='y', linestyle='--', linewidth=1.2)


# 获取所有图例元素，并去重
lines = []
labels = []
for ax in fig.axes:
    axLine, axLabel = ax.get_legend_handles_labels()
    for line, label in zip(axLine, axLabel):
        if label not in labels:  # 检查是否已存在相同的label
            lines.append(line)
            labels.append(label)

fig.legend(lines, labels,
           loc='upper center',
           ncol=4, bbox_to_anchor=(0.5, 0.95), fontsize=32)  # 图例的位置

# 调整子图布局
plt.tight_layout(rect=[0, 0, 1, 0.83])
# 保存图表
plt.savefig('../Figures/SimpleQ_all.pdf', dpi=360)

# 显示图表
plt.show()
