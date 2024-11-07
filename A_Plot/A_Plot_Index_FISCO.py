import matplotlib.pyplot as plt
from matplotlib import rcParams

config = {
    "font.family": 'serif',
    "font.size": 24,
    "mathtext.fontset": 'stix',
    "font.serif": ['Times New Roman'],
}
rcParams.update(config)

x = [16, 32, 64, 128, 256, 512, 1024]

Mulchain_v_CPU_Time_BTC = [0.5347, 0.5273, 0.5204, 0.5178, 0.5157, 0.5148, 0.5145]
Mulchain_o_CPU_Time_BTC = [0.1720, 0.1609, 0.1530, 0.1526, 0.1403, 0.1419, 0.1490]
Mulchain_v_CPU_Time_ETH = [0.5175, 0.5184, 0.5167, 0.5170, 0.5984, 0.5568, 0.5358]
Mulchain_o_CPU_Time_ETH = [0.1603, 0.1695, 0.1719, 0.1703, 0.1646, 0.1505, 0.1532]

# 创建图形和单个子图
fig, axs = plt.subplots(1, 2, figsize=(15, 6), dpi=360)

# 绘制 CPU Time vs Number (Blocks)
axs[0].plot(x, Mulchain_o_CPU_Time_BTC, marker='o', linestyle='-', color='black',
            label='MulChain$_{OB}$', markerfacecolor='none', markersize=10, linewidth=3.0)
axs[0].plot(x, Mulchain_o_CPU_Time_ETH, marker='s', linestyle='-', color='#33FF57',
            label='MulChain$_{OE}$', markerfacecolor='none', markersize=10, linewidth=3.0)
axs[0].plot(x, Mulchain_v_CPU_Time_BTC, marker='^', linestyle='-', color='#8B4513',
            label='MulChain$_{VB}$', markerfacecolor='none', markersize=10, linewidth=3.0)
axs[0].plot(x, Mulchain_v_CPU_Time_ETH, marker='D', linestyle='-', color='#A9A9A9',
            label='MulChain$_{VE}$', markerfacecolor='none', markersize=10, linewidth=3.0)

# 设置坐标轴
axs[0].set_xlabel('Number (Blocks)\n(a) Index Construction Cost', fontsize=28)
axs[0].set_ylabel('CPU time (s)', fontsize=28)
axs[0].set_xscale('log', base=2)  # 设置x轴为对数尺度，底数为2
axs[0].set_xticks(x)
axs[0].set_xticklabels(['$2^{4}$', '$2^{5}$', '$2^{6}$', '$2^{7}$', '$2^{8}$', '$2^{9}$', '$2^{10}$'])
axs[0].set_yscale('linear')  # 设置y轴为线性尺度
# axs[0].legend(loc='center right')
axs[0].grid(axis='x', linestyle='--', linewidth=1.2)
axs[0].grid(axis='y', linestyle='--', linewidth=1.2)


Mulchain_BT_latency_BTC = [0.62085688, 0.57566725, 0.57828022, 0.58273175, 0.58035325, 0.59804525, 0.61811837]
Mulchain_o_latency_BTC = [0.01165827, 0.01211797, 0.01182900, 0.01162278, 0.01229388, 0.01337736, 0.01583535]

Mulchain_BT_latency_ETH = [0.55680461, 0.53231013, 0.56093619, 0.55620986, 0.64964214, 0.61019251, 0.59350129]
Mulchain_o_latency_ETH = [0.00973159, 0.01008702, 0.01072713, 0.01101402, 0.01157666, 0.01271155, 0.01464972]

axs[1].plot(x, Mulchain_o_latency_BTC, marker='o', linestyle='-', color='black',
            label='MulChain$_{OB}$', markerfacecolor='none', markersize=10, linewidth=3.0)
axs[1].plot(x, Mulchain_o_latency_ETH, marker='s', linestyle='-', color='#33FF57',
            label='MulChain$_{OE}$', markerfacecolor='none', markersize=10, linewidth=3.0)
axs[1].plot(x, Mulchain_BT_latency_BTC, marker='v', linestyle='-', color='#FF4500',
            label='MulChain$_{BTB}$', markerfacecolor='none', markersize=10, linewidth=3.0)
axs[1].plot(x, Mulchain_BT_latency_ETH, marker='*', linestyle='-', color='#00008B',
            label='MulChain$_{BTE}$', markerfacecolor='none', markersize=10, linewidth=3.0)

axs[1].set_xlabel('Number (Blocks)\n(b) Latency', fontsize=28)
axs[1].set_ylabel('Latency (s)', fontsize=28)
axs[1].set_xscale('log', base=2)  # 设置x轴为对数尺度，底数为2
# axs[1].set_yscale('log')  # 设置y轴为对数尺度
# axs[1].set_yticks([1.42*10 ** -2, 1.48*10 ** -1, 1.54*10 ** 0],
#                   ['$10^{-2}$', '$10^{-1}$', '$10^{0}$'])
# axs[1].set_yticklabels(['$10^{-2}$', '$10^{-1}$', '$10^{0}$'], )
axs[1].set_xticks(x, ['$2^{4}$', '$2^{5}$', '$2^{6}$', '$2^{7}$', '$2^{8}$', '$2^{9}$', '$2^{10}$'])  # 设置X轴刻度
# axs[1].set_xticklabels(x, )
# axs[1].legend(loc='center right',)
axs[1].grid(axis='x', linestyle='--', linewidth=1.2)
axs[1].grid(axis='y', linestyle='--', linewidth=1.2)


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
           ncol=3, bbox_to_anchor=(0.5, 1.03), fontsize=28)  # 图例的位置
# 调整子图布局
plt.tight_layout(rect=[0, 0, 1, 0.85])


# 保存图表
plt.savefig('../Figures/FISCO_all.pdf', dpi=360)

# 显示图表
plt.show()
