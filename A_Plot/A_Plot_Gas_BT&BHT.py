import matplotlib.pyplot as plt
from matplotlib import rcParams

config = {
    "font.family": 'serif',
    "font.size": 24,
    "mathtext.fontset": 'stix',
    "font.serif": ['Times New Roman'],
}
rcParams.update(config)

x = [8, 16, 32, 64, 128, 256, 512]

# 创建图形和子图
fig, axs = plt.subplots(1, 2, figsize=(15, 5), dpi=360)

Mulchain_v_GAS_BTC = [397478, 564952, 976938, 1846130, 3600424, 7131044, 14242005]
Mulchain_bt_GAS_BTC = [102723, 102723, 102723, 102723, 102723, 102723, 102723]
Mulchain_bh_GAS_BTC = [102723, 89325, 82626, 79276, 77601, 76764, 76345]

Mulchain_v_GAS_BTC_div10 = [x / 100000 for x in Mulchain_v_GAS_BTC]
Mulchain_bt_GAS_BTC_div10 = [x / 100000 for x in Mulchain_bt_GAS_BTC]
Mulchain_bh_GAS_BTC_div10 = [x / 100000 for x in Mulchain_bh_GAS_BTC]

axs[0].plot(x, Mulchain_v_GAS_BTC_div10, marker='^', linestyle='-', color='blue',
            label='MulChain$_{V}$', markerfacecolor='none', markersize=10, linewidth=3.0)
axs[0].plot(x, Mulchain_bt_GAS_BTC_div10, marker='v', linestyle='-', color='#33FF57',
            label='MulChain$_{BT}$', markerfacecolor='none', markersize=10, linewidth=3.0)
axs[0].plot(x, Mulchain_bh_GAS_BTC_div10, marker='P', linestyle='-', color='#8B4513',
            label='MulChain$_{BH}$', markerfacecolor='none', markersize=10, linewidth=3.0)

axs[0].set_xlabel('Number (Blocks)\n(a) Gas Fee for Time Range Query', fontsize=28)
axs[0].set_ylabel('Gas Consumption(x$10^{5}$)', fontsize=28)
axs[0].set_xscale('log', base=2)  # 设置x轴为对数尺度，底数为2
axs[0].set_yscale('log')  # 设置y轴为对数尺度
axs[0].set_yticks([10 ** 0, 10 ** 1, 10 ** 2],
                  ['$10^{0}$', '$10^{1}$', '$10^{2}$'])
axs[0].set_yticklabels(['$10^{0}$', '$10^{1}$', '$10^{2}$'], )
axs[0].set_xticks(x,
                  ['$2^{3}$', '$2^{4}$', '$2^{5}$', '$2^{6}$', '$2^{7}$', '$2^{8}$', '$2^{9}$'])  # 设置X轴刻度

axs[0].legend(fontsize=16, loc='upper left')
axs[0].grid(axis='y', linestyle='--', linewidth=1.2)

Mulchain_v_GAS_BTC_1 = [47998.2500, 47998.5000, 47998.7273, 47998.8605, 47998.9298, 48003.4451, 48006.8257]
Mulchain_T_GAS_BTC = [76857, 81881, 80835.2656, 82928.6953, 81149.2734, 82902.5234, 99048.1289]

Mulchain_v_GAS_BTC_1_div10 = [x / 10000 for x in Mulchain_v_GAS_BTC_1]
Mulchain_T_GAS_BTC_div10 = [x / 10000 for x in Mulchain_T_GAS_BTC]

axs[1].plot(x, Mulchain_v_GAS_BTC_1_div10, marker='^', linestyle='-', color='blue',
            label='MulChain$_{V}$', markerfacecolor='none', markersize=10, linewidth=3.0)
axs[1].plot(x, Mulchain_T_GAS_BTC_div10, marker='v', linestyle='-', color='#FF4500',
            label='MulChain$_{T}$', markerfacecolor='none', markersize=10, linewidth=3.0)

axs[1].set_xlabel('Number (Blocks)\n(b) Gas Fee for Fuzzy Query', fontsize=28)
axs[1].set_ylabel('Gas Consumption(x$10^{4}$)', fontsize=28)
axs[1].set_xscale('log', base=2)  # 设置x轴为对数尺度，底数为2
# axs[1].set_yscale('log')  # 设置y轴为对数尺度
# axs[1].set_yticks([10 ** 0, 10 ** 1, 10 ** 2],
#                   ['$10^{0}$', '$10^{1}$', '$10^{2}$'])
# axs[1].set_yticklabels(['$10^{0}$', '$10^{1}$', '$10^{2}$'], )
axs[1].set_xticks(x,
                  ['$2^{3}$', '$2^{4}$', '$2^{5}$', '$2^{6}$', '$2^{7}$', '$2^{8}$', '$2^{9}$'])  # 设置X轴刻度

axs[1].legend(fontsize=16, loc='upper left')
axs[1].grid(axis='y', linestyle='--', linewidth=1.2)

# lines = []
# labels = []
# for ax in fig.axes:
#     axLine, axLabel = ax.get_legend_handles_labels()
#     for line, label in zip(axLine, axLabel):
#         if label not in labels:  # 检查是否已存在相同的label
#             lines.append(line)
#             labels.append(label)
#
# fig.legend(lines, labels,
#            loc='upper center',
#            ncol=4, bbox_to_anchor=(0.5, 1.02))

# 调整子图布局
# plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.tight_layout()

# 保存图表
plt.savefig('../Figures/Gas_BHT_BT.pdf', dpi=360)

# 显示图表
plt.show()
