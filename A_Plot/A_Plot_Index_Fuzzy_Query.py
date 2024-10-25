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

Mulchain_v_CPU_Time_BTC = [2.4012, 2.3651, 2.3570, 2.3309, 2.3486, 2.3427, 2.3475]
Mulchain_o_CPU_Time_BTC = [2.3879, 2.3584, 2.3537, 2.3292, 2.3478, 2.3422, 2.3473]
Mulchain_v_CPU_Time_ETH = [2.3822, 2.3233, 2.3087, 2.3111, 2.3438, 2.3760, 2.3877]
Mulchain_o_CPU_Time_ETH = [2.3657, 2.3150, 2.3046, 2.3090, 2.3428, 2.3755, 2.3875]

# 创建图形和子图
fig, axs = plt.subplots(1, 3, figsize=(21, 9), dpi=360)

# 第1个子图：CPU Time vs Number (Blocks)
axs[0].plot(x, Mulchain_o_CPU_Time_BTC, marker='o', linestyle='-', color='#C6B3D3',
            label='MulChain$_{OB}$', markerfacecolor='none')
axs[0].plot(x, Mulchain_o_CPU_Time_ETH, marker='s', linestyle='-', color='#80BA8A',
            label='MulChain$_{OE}$', markerfacecolor='none')
axs[0].plot(x, Mulchain_v_CPU_Time_BTC, marker='^', linestyle='-', color='#9CD1C8',
            label='MulChain$_{VB}$', markerfacecolor='none')
axs[0].plot(x, Mulchain_v_CPU_Time_ETH, marker='D', linestyle='-', color='#6BB7CA',
            label='MulChain$_{VE}$', markerfacecolor='none')

# 设置第一个子图的坐标轴
axs[0].set_xlabel('Number (Blocks)\n(a) Insert Cost', )
axs[0].set_ylabel('CPU time (s)', )
axs[0].set_xscale('log', base=2)  # 设置x轴为对数尺度，底数为2
axs[0].set_xticks(x,
                  ['$2^{3}$', '$2^{4}$', '$2^{5}$', '$2^{6}$', '$2^{7}$', '$2^{8}$', '$2^{9}$'])  # 设置X轴刻度
axs[0].set_yscale('linear')  # 设置y轴为对数尺度
axs[0].set_yticks([2, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6])
axs[0].legend(fontsize=16, loc='upper center', bbox_to_anchor=(0.5, 1.18), ncol=2)
axs[0].grid(axis='y', linestyle='--', linewidth=0.7)

# 第2个子图：Latency vs Number (Blocks)
Mulchain_v_latency_BTC = [0.3803, 0.5719, 1.0186, 1.9726, 3.9202, 7.8390, 15.8249]
Mulchain_Tr_latency_BTC = [0.0298, 0.0455, 0.0380, 0.0381, 0.0399, 0.0403, 0.0466]
Mulchain_o_latency_BTC = [0.0298, 0.0302, 0.0304, 0.0306, 0.0304, 0.0309, 0.0339]

Mulchain_v_latency_ETH = [0.5325, 0.7084, 1.1328, 2.0620, 4.0100, 7.9133, 16.1916]
Mulchain_Tr_latency_ETH = [0.2345, 0.2494, 0.2330, 0.2232, 0.3397, 0.4468, 0.8243]
Mulchain_o_latency_ETH = [0.0839, 0.0987, 0.1120, 0.1289, 0.2434, 0.3640, 0.7355]

axs[1].plot(x, Mulchain_o_latency_BTC, marker='o', linestyle='-', color='#C6B3D3',
            label='MulChain$_{OB}$', markerfacecolor='none')
axs[1].plot(x, Mulchain_o_latency_ETH, marker='s', linestyle='-', color='#80BA8A',
            label='MulChain$_{OE}$', markerfacecolor='none')
axs[1].plot(x, Mulchain_v_latency_BTC, marker='^', linestyle='-', color='#9CD1C8',
            label='MulChain$_{VB}$', markerfacecolor='none')
axs[1].plot(x, Mulchain_v_latency_ETH, marker='D', linestyle='-', color='#6BB7CA',
            label='MulChain$_{VE}$', markerfacecolor='none')
axs[1].plot(x, Mulchain_Tr_latency_BTC, marker='v', linestyle='-', color='#ED9F9B',
            label='MulChain$_{BTB}$', markerfacecolor='none')
axs[1].plot(x, Mulchain_Tr_latency_ETH, marker='*', linestyle='-', color='#EEC79F',
            label='MulChain$_{BTE}$', markerfacecolor='none')

axs[1].set_xlabel('Number (Blocks)\n(b) Latency', )
axs[1].set_ylabel('Latency (s)', )
axs[1].set_xscale('log', base=2)  # 设置x轴为对数尺度，底数为2
axs[1].set_yscale('log')  # 设置y轴为对数尺度
axs[1].set_yticks([10 ** -2, 10 ** -1.5, 10 ** -1, 10 ** 0],
                  ['$10^{-2}$', '$10^{-1.5}$', '$10^{-1}$', '$10^{0}$'])
axs[1].set_yticklabels(['$10^{-2}$', '$10^{-1.5}$', '$10^{-1}$', '$10^{0}$'], )
axs[1].set_xticks(x,
                  ['$2^{3}$', '$2^{4}$', '$2^{5}$', '$2^{6}$', '$2^{7}$', '$2^{8}$', '$2^{9}$'])  # 设置X轴刻度
# axs[1].set_xticklabels(x, )
axs[1].legend(fontsize=16, loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=2)
axs[1].grid(axis='y', linestyle='--', linewidth=0.7)

# 子坐标系显示范围
# axins = axs[1].inset_axes((0.21, 0.71, 0.35, 0.28))
# axins.plot(x, Mulchain_o_latency_BTC, marker='o', linestyle='-', color='#C6B3D3',
#            label='MulChain$_{OB}$', markerfacecolor='none')
# axins.plot(x, Mulchain_o_latency_ETH, marker='s', linestyle='-', color='#80BA8A',
#            label='MulChain$_{OE}$', markerfacecolor='none')
# axins.plot(x, Mulchain_Tr_latency_BTC, marker='v', linestyle='-', color='#ED9F9B',
#            label='MulChain$_{BTB}$', markerfacecolor='none')
# axins.plot(x, Mulchain_Tr_latency_ETH, marker='*', linestyle='-', color='#EEC79F',
#            label='MulChain$_{BTE}$', markerfacecolor='none')
# axins.set_xscale('log', base=2)  # 设置x轴为对数尺度，底数为2
# axins.set_xticks(x)  # 设置X轴刻度
# axins.set_yscale('log')  # 设置y轴为对数尺度
# zone_left = 4
# zone_right = 6

# 坐标轴的扩展比例（根据实际数据调整）
# x_ratio = 0.1  # x轴显示范围的扩展比例
# y_ratio = 0.5  # y轴显示范围的扩展比例

# X轴的显示范围
# xlim0 = x[zone_left] - (x[zone_right] - x[zone_left]) * x_ratio
# xlim1 = x[zone_right] + (x[zone_right] - x[zone_left]) * x_ratio

# Y轴的显示范围
# y = np.hstack((Mulchain_Tr_latency_BTC[zone_left:zone_right],
#                Mulchain_Tr_latency_ETH[zone_left:zone_right]))
# ylim0 = np.min(y) - (np.max(y) - np.min(y)) * y_ratio
# ylim1 = np.max(y) + (np.max(y) - np.min(y)) * y_ratio

# 调整子坐标系的显示范围
# axins.set_xlim(xlim0, xlim1)
# axins.set_ylim(ylim0, ylim1)
# mark_inset(axs[1], axins, loc1=3, loc2=1, fc="none", ec='k', lw=0.5)

# 第3个子图：VO Size vs Number (Blocks)
Mulchain_v_VO_BTC = [76.7972, 76.7976, 76.7980, 76.7982, 76.7983, 76.8055, 76.8109]
Mulchain_Tr_VO_BTC = [122.9724, 131.0111, 129.3364, 132.6859, 129.8388, 132.6440, 158.4770]

Mulchain_v_VO_ETH = [98.2340, 98.2344, 98.2348, 98.2350, 98.2351, 98.2423, 98.2477]
Mulchain_Tr_VO_ETH = [784.8311, 1015.9459, 1211.2209, 1475.3281, 3246.8717, 5071.3371, 10552.3957]

axs[2].plot(x, Mulchain_v_VO_BTC, marker='^', linestyle='-', color='#9CD1C8',
            label='MulChain$_{VB}$', markerfacecolor='none')
axs[2].plot(x, Mulchain_v_VO_ETH, marker='D', linestyle='-', color='#6BB7CA',
            label='MulChain$_{VE}$', markerfacecolor='none')
axs[2].plot(x, Mulchain_Tr_VO_BTC, marker='v', linestyle='-', color='#ED9F9B',
            label='MulChain$_{BTB}$', markerfacecolor='none')
axs[2].plot(x, Mulchain_Tr_VO_ETH, marker='*', linestyle='-', color='#EEC79F',
            label='MulChain$_{BTE}$', markerfacecolor='none')


# 设置第三个子图的坐标轴
axs[2].set_xlabel('Number (Blocks)\n(c) VO Size', )
axs[2].set_ylabel('VO Size (KB)', )
axs[2].set_xscale('log', base=2)  # 设置x轴为对数尺度，底数为2
axs[2].set_yscale('log')  # 设置y轴为对数尺度
axs[2].set_xticks(x,
                  ['$2^{3}$', '$2^{4}$', '$2^{5}$', '$2^{6}$', '$2^{7}$', '$2^{8}$', '$2^{9}$'])  # 设置X轴刻度

axs[2].legend(fontsize=16, loc='upper center', bbox_to_anchor=(0.5, 1.18), ncol=2)
axs[2].grid(axis='y', linestyle='--', linewidth=0.7)

# 调整子图布局
plt.tight_layout()

# 保存图表
plt.savefig('../Figures/FuzzyQ_all.pdf', dpi=360)

# 显示图表
plt.show()
