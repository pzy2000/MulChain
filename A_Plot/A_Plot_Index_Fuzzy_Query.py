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

Mulchain_v_CPU_Time_BTC = [2.4012, 2.3651, 2.3570, 2.3309, 2.3486, 2.3427, 2.3475]
Mulchain_o_CPU_Time_BTC = [2.3879, 2.3584, 2.3537, 2.3292, 2.3478, 2.3422, 2.3473]
Mulchain_v_CPU_Time_ETH = [2.3822, 2.3233, 2.3087, 2.3111, 2.3438, 2.3760, 2.3877]
Mulchain_o_CPU_Time_ETH = [2.3657, 2.3150, 2.3046, 2.3090, 2.3428, 2.3755, 2.3875]

# 创建图形和子图
fig, axs = plt.subplots(1, 4, figsize=(28, 7), dpi=360)

# 第1个子图：CPU Time vs Number (Blocks)
axs[0].plot(x, Mulchain_o_CPU_Time_BTC, marker='o', linestyle='-', color='yellow',
            label='MulChain$_{OB}$', markerfacecolor='none', markersize=10, linewidth=3.0)
axs[0].plot(x, Mulchain_o_CPU_Time_ETH, marker='s', linestyle='-', color='#33FF57',
            label='MulChain$_{OE}$', markerfacecolor='none', markersize=10, linewidth=3.0)
axs[0].plot(x, Mulchain_v_CPU_Time_BTC, marker='^', linestyle='-', color='#8B4513',
            label='MulChain$_{VB}$', markerfacecolor='none', markersize=10, linewidth=3.0)
axs[0].plot(x, Mulchain_v_CPU_Time_ETH, marker='D', linestyle='-', color='#A9A9A9',
            label='MulChain$_{VE}$', markerfacecolor='none', markersize=10, linewidth=3.0)

# 设置第一个子图的坐标轴
axs[0].set_xlabel('Number (Blocks)\n(a) Insert Cost', )
axs[0].set_ylabel('CPU time (s)', )
axs[0].set_xscale('log', base=2)  # 设置x轴为对数尺度，底数为2
axs[0].set_xticks(x)
axs[0].set_xticklabels(['$2^{4}$', '$2^{5}$', '$2^{6}$', '$2^{7}$',
                        '$2^{8}$', '$2^{9}$', '$2^{10}$'])
axs[0].set_yscale('linear')  # 设置y轴为线性尺度
axs[0].set_yticks([2.3, 2.34, 2.38])
axs[0].grid(axis='x', linestyle='--', linewidth=1.2)
axs[0].grid(axis='y', linestyle='--', linewidth=1.2)

# 第2个子图：Latency vs Number (Blocks)
Mulchain_v_latency_BTC = [0.3803, 0.5719, 1.0186, 1.9726, 3.9202, 7.8390, 15.8249]
Mulchain_Tr_latency_BTC = [0.0298, 0.0455, 0.0380, 0.0381, 0.0399, 0.0403, 0.0466]
Mulchain_o_latency_BTC = [0.0298, 0.0302, 0.0304, 0.0306, 0.0304, 0.0309, 0.0339]

Mulchain_v_latency_ETH = [0.5325, 0.7084, 1.1328, 2.0620, 4.0100, 7.9133, 16.1916]
Mulchain_Tr_latency_ETH = [0.2345, 0.2494, 0.2330, 0.2232, 0.3397, 0.4468, 0.8243]
Mulchain_o_latency_ETH = [0.0839, 0.0987, 0.1120, 0.1289, 0.2434, 0.3640, 0.7355]

axs[1].plot(x, Mulchain_o_latency_BTC, marker='o', linestyle='-', color='yellow',
            label='MulChain$_{OB}$', markerfacecolor='none', markersize=10, linewidth=3.0)
axs[1].plot(x, Mulchain_o_latency_ETH, marker='s', linestyle='-', color='#33FF57',
            label='MulChain$_{OE}$', markerfacecolor='none', markersize=10, linewidth=3.0)
axs[1].plot(x, Mulchain_v_latency_BTC, marker='^', linestyle='-', color='#8B4513',
            label='MulChain$_{VB}$', markerfacecolor='none', markersize=10, linewidth=3.0)
axs[1].plot(x, Mulchain_v_latency_ETH, marker='D', linestyle='-', color='#A9A9A9',
            label='MulChain$_{VE}$', markerfacecolor='none', markersize=10, linewidth=3.0)
axs[1].plot(x, Mulchain_Tr_latency_BTC, marker='v', linestyle='-', color='#A34CFF',
            label='MulChain$_{TB}$', markerfacecolor='none', markersize=10, linewidth=3.0)
axs[1].plot(x, Mulchain_Tr_latency_ETH, marker='*', linestyle='-', color='#4CFFFF',
            label='MulChain$_{TE}$', markerfacecolor='none', markersize=10, linewidth=3.0)

axs[1].set_xlabel('Number (Blocks)\n(b) Latency', )
axs[1].set_ylabel('Latency (s)', )
axs[1].set_xscale('log', base=2)  # 设置x轴为对数尺度，底数为2
axs[1].set_yscale('log')  # 设置y轴为对数尺度
axs[1].set_yticks([10 ** -2, 10 ** -1, 10 ** 0],
                  ['$10^{-2}$', '$10^{-1}$', '$10^{0}$'])
axs[1].set_xticks(x)
axs[1].set_xticklabels(['$2^{4}$', '$2^{5}$', '$2^{6}$', '$2^{7}$',
                        '$2^{8}$', '$2^{9}$', '$2^{10}$'])
axs[1].grid(axis='x', linestyle='--', linewidth=1.2)
axs[1].grid(axis='y', linestyle='--', linewidth=1.2)

# 第3个子图：VO Size vs Number (Blocks)
Mulchain_v_VO_BTC = [76.7972, 76.7976, 76.7980, 76.7982, 76.7983, 76.8055, 76.8109]
Mulchain_Tr_VO_BTC = [122.9724, 131.0111, 129.3364, 132.6859, 129.8388, 132.6440, 158.4770]

Mulchain_v_VO_ETH = [98.2340, 98.2344, 98.2348, 98.2350, 98.2351, 98.2423, 98.2477]
Mulchain_Tr_VO_ETH = [784.8311, 1015.9459, 1211.2209, 1475.3281, 3246.8717, 5071.3371, 10552.3957]

axs[2].plot(x, Mulchain_v_VO_BTC, marker='^', linestyle='-', color='#8B4513',
            label='MulChain$_{VB}$', markerfacecolor='none', markersize=10, linewidth=3.0)
axs[2].plot(x, Mulchain_v_VO_ETH, marker='D', linestyle='-', color='#A9A9A9',
            label='MulChain$_{VE}$', markerfacecolor='none', markersize=10, linewidth=3.0)
axs[2].plot(x, Mulchain_Tr_VO_BTC, marker='v', linestyle='-', color='#A34CFF',
            label='MulChain$_{TB}$', markerfacecolor='none', markersize=10, linewidth=3.0)
axs[2].plot(x, Mulchain_Tr_VO_ETH, marker='*', linestyle='-', color='#4CFFFF',
            label='MulChain$_{TE}$', markerfacecolor='none', markersize=10, linewidth=3.0)

# 设置第三个子图的坐标轴
axs[2].set_xlabel('Number (Blocks)\n(c) VO Size', )
axs[2].set_ylabel('VO Size (KB)', )
axs[2].set_xscale('log', base=2)  # 设置x轴为对数尺度，底数为2
axs[2].set_yscale('log')  # 设置y轴为对数尺度
axs[2].set_xticks(x)
axs[2].set_xticklabels(['$2^{4}$', '$2^{5}$', '$2^{6}$', '$2^{7}$',
                        '$2^{8}$', '$2^{9}$', '$2^{10}$'])
axs[2].grid(axis='x', linestyle='--', linewidth=1.2)
axs[2].grid(axis='y', linestyle='--', linewidth=1.2)

# 第4个子图：平均VO Size倍数和Latency倍数 vs Number (Blocks)
# 计算VO Size倍数和Latency倍数
VO_Size_ETH = [Mulchain_Tr_VO_ETH[i] / Mulchain_v_VO_ETH[i] for i in range(len(x))]
VO_Size_BTC = [Mulchain_Tr_VO_BTC[i] / Mulchain_v_VO_BTC[i] for i in range(len(x))]
VO_Size_avg = [(VO_Size_ETH[i] + VO_Size_BTC[i]) / 2 for i in range(len(x))]

Latency_ETH = [Mulchain_Tr_latency_ETH[i] / Mulchain_v_latency_ETH[i] for i in range(len(x))]
Latency_BTC = [Mulchain_Tr_latency_BTC[i] / Mulchain_v_latency_BTC[i] for i in range(len(x))]
Latency_avg = [(Latency_ETH[i] + Latency_BTC[i]) / 2 for i in range(len(x))]

# 绘制平均VO Size倍数
axs[3].plot(x, VO_Size_avg, marker='o', linestyle='-', color='blue',
            label='Average VO Size Ratio', markerfacecolor='none', markersize=10, linewidth=3.0)

# 创建右侧的y轴并绘制平均Latency倍数
ax3_right = axs[3].twinx()
ax3_right.plot(x, Latency_avg, marker='s', linestyle='--', color='red',
               label='Average Latency Ratio', markerfacecolor='none', markersize=10, linewidth=3.0)

# 设置第四个子图的坐标轴
axs[3].set_xlabel('Number (Blocks)\n(d) Average Ratios', )
axs[3].set_ylabel('Average VO Size Ratio', color='blue')
ax3_right.set_ylabel('Average Latency Ratio', color='red')

# 设置x轴为对数尺度，底数为2
axs[3].set_xscale('log', base=2)
axs[3].set_xticks(x)
axs[3].set_xticklabels(['$2^{4}$', '$2^{5}$', '$2^{6}$', '$2^{7}$',
                        '$2^{8}$', '$2^{9}$', '$2^{10}$'])

# 设置y轴为对数尺度
axs[3].set_yscale('log')
axs[3].set_yticks([10 ** 0, 10 ** 1, 10 ** 2],
                  ['$10^{0}$', '$10^{1}$', '$10^{2}$'])
ax3_right.set_yscale('log')
ax3_right.set_yticks([10 ** -2, 10 ** -1, 10 ** 0],
                     ['$10^{-2}$', '$10^{-1}$', '$10^{0}$'])

# 设置y轴颜色
axs[3].tick_params(axis='y', colors='blue')
ax3_right.tick_params(axis='y', colors='red')
# ax3_right.legend(loc='upper right')

# 添加网格线
axs[3].grid(axis='x', linestyle='--', linewidth=1.2)
axs[3].grid(axis='y', linestyle='--', linewidth=1.2)
# axs[3].legend(loc='upper right')

# 获取所有图例元素，并去重
lines = []
labels = []
for ax in [axs[0], axs[1], axs[2]]:
    axLine, axLabel = ax.get_legend_handles_labels()
    for line, label in zip(axLine, axLabel):
        if label not in labels:  # 检查是否已存在相同的label
            lines.append(line)
            labels.append(label)

# 添加第四个子图的图例元素
line1, label1 = axs[3].get_legend_handles_labels()
line2, label2 = ax3_right.get_legend_handles_labels()
lines.extend(line1 + line2)
labels.extend(label1 + label2)

# 创建总的图例
fig.legend(lines, labels,
           loc='upper center',
           ncol=4, bbox_to_anchor=(0.5, 1.02))

# 调整子图布局
plt.tight_layout(rect=[0, 0, 1, 0.89])

# 保存图表
plt.savefig('../Figures/FuzzyQ_all.pdf', dpi=360)

# 显示图表
plt.show()
