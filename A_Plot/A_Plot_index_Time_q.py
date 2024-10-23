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

Mulchain_v_CPU_Time_BTC = [2.4256, 2.3633, 2.3155, 2.3315, 2.3282, 2.3318, 2.3231]
Mulchain_o_CPU_Time_BTC = [2.3923, 2.3466, 2.3071, 2.3273, 2.3261, 2.3307, 2.3226]
Mulchain_v_CPU_Time_ETH = [2.3930, 2.3608, 2.3076, 2.3047, 2.3190, 2.3378, 2.3622]
Mulchain_o_CPU_Time_ETH = [2.3607, 2.3446, 2.2996, 2.3007, 2.3170, 2.3368, 2.3617]

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
axs[0].set_xticks(x)  # 设置X轴刻度
axs[0].set_xticklabels(x, )
axs[0].set_yscale('linear')  # 设置y轴为对数尺度
axs[0].set_yticks([2, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6])
# axs[0].set_yticklabels(['$10^{-0}$', '$10^{1}$'], )
axs[0].legend(fontsize=16, loc='upper center', bbox_to_anchor=(0.5, 1.18), ncol=2)
axs[0].grid(axis='y', linestyle='--', linewidth=0.7)

# 第2个子图：Latency vs Number (Blocks)
Mulchain_v_latency_BTC = [0.0888, 0.1165, 0.1896, 0.3443, 0.6559, 1.2873, 2.5559]
Mulchain_bt_latency_BTC = [0.0371, 0.0349, 0.0341, 0.0344, 0.0343, 0.0345, 0.0346]
Mulchain_bh_latency_BTC = [0.0335, 0.0330, 0.0322, 0.0328, 0.0329, 0.0327, 0.0333]
Mulchain_o_latency_BTC = [0.0335, 0.0330, 0.0322, 0.0328, 0.0329, 0.0327, 0.0333]

Mulchain_v_latency_ETH = [0.0950, 0.1206, 0.1930, 0.3505, 0.6709, 1.3139, 2.6067]
Mulchain_bt_latency_ETH = [0.0337, 0.0335, 0.0333, 0.0335, 0.0340, 0.0344, 0.0346]
Mulchain_bh_latency_ETH = [0.0324, 0.0333, 0.0325, 0.0326, 0.0327, 0.0330, 0.0333]
Mulchain_o_latency_ETH = [0.0324, 0.0333, 0.0325, 0.0326, 0.0327, 0.0330, 0.0333]

axs[1].plot(x, Mulchain_o_latency_BTC, marker='o', linestyle='-', color='#C6B3D3',
            label='MulChain$_{OB}$', markerfacecolor='none')
axs[1].plot(x, Mulchain_o_latency_ETH, marker='s', linestyle='-', color='#80BA8A',
            label='MulChain$_{OE}$', markerfacecolor='none')
axs[1].plot(x, Mulchain_v_latency_BTC, marker='^', linestyle='-', color='#9CD1C8',
            label='MulChain$_{VB}$', markerfacecolor='none')
axs[1].plot(x, Mulchain_v_latency_ETH, marker='D', linestyle='-', color='#6BB7CA',
            label='MulChain$_{VE}$', markerfacecolor='none')
axs[1].plot(x, Mulchain_bt_latency_BTC, marker='v', linestyle='-', color='#ED9F9B',
            label='MulChain$_{BTB}$', markerfacecolor='none')
axs[1].plot(x, Mulchain_bt_latency_ETH, marker='*', linestyle='-', color='#EEC79F',
            label='MulChain$_{BTE}$', markerfacecolor='none')
axs[1].plot(x, Mulchain_bh_latency_BTC, marker='P', linestyle='-', color='#F1DFA4',
            label='MulChain$_{BHB}$', markerfacecolor='none')
axs[1].plot(x, Mulchain_bh_latency_ETH, marker='X', linestyle='-', color='#DBE0ED',
            label='MulChain$_{BHE}$', markerfacecolor='none')

axs[1].set_xlabel('Number (Blocks)\n(b) Latency', )
axs[1].set_ylabel('Latency (s)', )
# axs[1].set_xscale('log', base=2)  # 设置x轴为对数尺度，底数为2
axs[1].set_yscale('log')  # 设置y轴为对数尺度
axs[1].set_yticks([10 ** -2, 10 ** -1.5, 10 ** -1, 10 ** 0],
                  ['$10^{-2}$', '$10^{-1.5}$', '$10^{-1}$', '$10^{0}$'])
axs[1].set_yticklabels(['$10^{-2}$', '$10^{-1.5}$', '$10^{-1}$', '$10^{0}$'], )
axs[1].set_xticks(x)  # 设置X轴刻度
axs[1].set_xticklabels(x, )
axs[1].legend(fontsize=16, loc='upper center', bbox_to_anchor=(0.5, 1.3), ncol=2)
axs[1].grid(axis='y', linestyle='--', linewidth=0.7)

# 子坐标系显示范围
axins = axs[1].inset_axes((0.21, 0.71, 0.35, 0.28))
axins.plot(x, Mulchain_bt_latency_BTC, marker='v', linestyle='-', color='#ED9F9B',
           label='MulChain$_{BTB}$', markerfacecolor='none')
axins.plot(x, Mulchain_bt_latency_ETH, marker='*', linestyle='-', color='#EEC79F',
           label='MulChain$_{BTE}$', markerfacecolor='none')
axins.plot(x, Mulchain_bh_latency_BTC, marker='P', linestyle='-', color='#F1DFA4',
           label='MulChain$_{BHB}$', markerfacecolor='none')
axins.plot(x, Mulchain_bh_latency_ETH, marker='X', linestyle='-', color='#DBE0ED',
           label='MulChain$_{BHE}$', markerfacecolor='none')
axins.set_xscale('log', base=2)  # 设置x轴为对数尺度，底数为2
# axins.set_xticks(x)  # 设置X轴刻度
# axins.set_yscale('log')  # 设置y轴为对数尺度
zone_left = 4
zone_right = 6

# 坐标轴的扩展比例（根据实际数据调整）
x_ratio = 0.1  # x轴显示范围的扩展比例
y_ratio = 0.5  # y轴显示范围的扩展比例

# X轴的显示范围
xlim0 = x[zone_left] - (x[zone_right] - x[zone_left]) * x_ratio
xlim1 = x[zone_right] + (x[zone_right] - x[zone_left]) * x_ratio

# Y轴的显示范围
y = np.hstack((Mulchain_bt_latency_BTC[zone_left:zone_right],
               Mulchain_bt_latency_ETH[zone_left:zone_right],
               Mulchain_bh_latency_BTC[zone_left:zone_right],
               Mulchain_bh_latency_ETH[zone_left:zone_right]))
ylim0 = np.min(y) - (np.max(y) - np.min(y)) * y_ratio
ylim1 = np.max(y) + (np.max(y) - np.min(y)) * y_ratio

# 调整子坐标系的显示范围
axins.set_xlim(xlim0, xlim1)
axins.set_ylim(ylim0, ylim1)
mark_inset(axs[1], axins, loc1=3, loc2=1, fc="none", ec='k', lw=0.5)

# 第3个子图：VO Size vs Number (Blocks)
Mulchain_v_VO_BTC = [635.9648, 903.9232, 1563.1016, 2953.8084, 5760.6786, 11409.6719, 22787.2088]
Mulchain_bt_VO_BTC = [164.3568, 164.3568, 164.3568, 164.3568, 164.3568, 164.3568, 164.3568]
Mulchain_bh_VO_BTC = [164.3568, 142.9200, 132.2016, 126.8424, 124.1628, 122.8230, 122.1531]

Mulchain_v_VO_ETH = [657.4016, 936.0784, 1632.7712, 3095.8264, 6056.7724, 12006.8006, 23985.2363]
Mulchain_bt_VO_ETH = [164.3568, 164.3568, 164.3568, 164.3568, 164.3568, 164.3568, 164.3568]
Mulchain_bh_VO_ETH = [164.3568, 142.9200, 132.2016, 126.8424, 124.1628, 122.8230, 122.1531]

axs[2].plot(x, Mulchain_v_VO_BTC, marker='^', linestyle='-', color='#9CD1C8',
            label='MulChain$_{VB}$', markerfacecolor='none')
axs[2].plot(x, Mulchain_v_VO_ETH, marker='D', linestyle='-', color='#6BB7CA',
            label='MulChain$_{VE}$', markerfacecolor='none')
axs[2].plot(x, Mulchain_bt_VO_BTC, marker='v', linestyle='-', color='#ED9F9B',
            label='MulChain$_{BTB}$', markerfacecolor='none')
axs[2].plot(x, Mulchain_bt_VO_ETH, marker='*', linestyle='-', color='#EEC79F',
            label='MulChain$_{BTE}$', markerfacecolor='none')
axs[2].plot(x, Mulchain_bh_VO_BTC, marker='P', linestyle='-', color='#F1DFA4',
            label='MulChain$_{BHB}$', markerfacecolor='none')
axs[2].plot(x, Mulchain_bh_VO_ETH, marker='X', linestyle='-', color='#DBE0ED',
            label='MulChain$_{BHE}$', markerfacecolor='none')

# 设置第三个子图的坐标轴
axs[2].set_xlabel('Number (Blocks)\n(c) VO Size', )
axs[2].set_ylabel('VO Size (KB)', )
axs[2].set_xscale('log', base=2)  # 设置x轴为对数尺度，底数为2
axs[2].set_yscale('log')  # 设置y轴为对数尺度
axs[2].set_xticks(x)  # 设置X轴刻度
axs[2].set_xticklabels(x, )
axs[2].legend(fontsize=16, loc='upper center', bbox_to_anchor=(0.5, 1.18), ncol=3)
axs[2].grid(axis='y', linestyle='--', linewidth=0.7)

# 调整子图布局
plt.tight_layout()

# 保存图表
plt.savefig('../Figures/TimeQ_all.pdf', dpi=360)

# 显示图表
plt.show()
