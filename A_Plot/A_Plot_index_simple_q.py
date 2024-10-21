import matplotlib.pyplot as plt
from matplotlib import rcParams

config = {
    "font.family": 'serif',
    "font.size": 20,
    "mathtext.fontset": 'stix',
    "font.serif": ['Times New Roman'],
}
rcParams.update(config)

x = [16, 32, 64, 128, 256, 512, 1024]
Mulchain_v_CPU_Time_BTC = [1.1791, 1.2663, 1.2252, 1.1812, 1.1535, 1.1452, 1.1513]
Mulchain_o_CPU_Time_BTC = [1.1651, 1.2592, 1.2216, 1.1795, 1.1526, 1.1448, 1.1511]

Mulchain_v_CPU_Time_ETH = [1.2250, 1.3253, 1.2882, 1.2566, 1.2387, 1.2392, 1.2406]
Mulchain_o_CPU_Time_ETH = [1.2117, 1.3186, 1.2849, 1.2550, 1.2379, 1.2387, 1.2404]

# 动态计算每个柱状的宽度
widths_bar = [value / 8 for value in x]

# 创建图形和子图
fig, axs = plt.subplots(1, 3, figsize=(18, 5), dpi=360)

# 第1个子图：CPU Time vs Number (Blocks)
bar1 = [value - w for value, w in zip(x, widths_bar)]  # 左侧的柱状位置
bar4 = [value for value, w in zip(x, widths_bar)]  # 右侧的柱状位置

bar2 = [value + w for value, w in zip(x, widths_bar)]  # mid的柱状位置
bar3 = [value + 2 * w for value, w in zip(x, widths_bar)]  # 右侧的柱状位置

axs[0].bar(bar1, Mulchain_o_CPU_Time_BTC, color='#C6B3D3', width=widths_bar,
           label='MulChain$_OB$')
axs[0].bar(bar4, Mulchain_o_CPU_Time_ETH, color='#80BA8A', width=widths_bar,
           label='MulChain$_OE$')
axs[0].bar(bar2, Mulchain_v_CPU_Time_BTC, color='#9CD1C8', width=widths_bar,
           label='MulChain$_VB$')
axs[0].bar(bar3, Mulchain_v_CPU_Time_ETH, color='#6BB7CA', width=widths_bar,
           label='MulChain$_VE$')

# 设置第一个子图的坐标轴
axs[0].set_xlabel('Number (Blocks)\n(a) Insert Cost', fontsize=20)
axs[0].set_ylabel('CPU time (s)', fontsize=20)
axs[0].set_xscale('log', base=2)  # 设置x轴为对数制度，底数为2
axs[0].set_xticks(x)  # 设置X轴制点
axs[0].set_xticklabels(x, fontsize=20)

axs[0].legend(fontsize=12, loc='upper center', bbox_to_anchor=(0.5, 1.25), ncol=2)
axs[0].grid(axis='y', linestyle='--', linewidth=0.7)





# 第2个子图：Query Latency vs Number (Blocks)
Mulchain_v_latency_BTC = [0.6284, 0.6030, 0.6061, 0.6040, 0.6193, 0.6197, 0.5977]
Mulchain_o_latency_BTC = [0.0259, 0.0274, 0.0253, 0.0245, 0.0241, 0.0240, 0.0238]

Mulchain_v_latency_ETH = [0.6317, 0.6089, 0.6102, 0.6057, 0.6215, 0.6223, 0.5986]
Mulchain_o_latency_ETH = [0.0237, 0.0269, 0.0253, 0.0243, 0.0241, 0.0241, 0.0238]
bar5 = [value - w for value, w in zip(x, widths_bar)]  # 左侧的柱状位置
bar6 = [value for value, w in zip(x, widths_bar)]  # 左侧的柱状位置
bar7 = [value + w for value, w in zip(x, widths_bar)]  # 右侧的柱状位置
bar8 = [value + 2 * w for value, w in zip(x, widths_bar)]  # 右侧的柱状位置
axs[1].bar(bar5, Mulchain_o_latency_BTC, color='#C6B3D3', width=widths_bar,
           label='MulChain$_OB$')
axs[1].bar(bar6, Mulchain_o_latency_ETH, color='#80BA8A', width=widths_bar,
           label='MulChain$_OE$')
axs[1].bar(bar7, Mulchain_v_latency_BTC, color='#9CD1C8', width=widths_bar,
           label='MulChain$_VB$')
axs[1].bar(bar8, Mulchain_v_latency_ETH, color='#6BB7CA', width=widths_bar,
           label='MulChain$_VE$')


axs[1].set_xlabel('Number (Blocks)\n(b) Query Latency', fontsize=20)
axs[1].set_ylabel('Query Latency (s)', fontsize=20)
axs[1].set_xscale('log', base=2)  # 设置x轴为对数制度，底数为2

axs[1].set_xticks(x)  # 设置X轴制点

axs[1].set_xticklabels(x, fontsize=20)

axs[1].legend(fontsize=12, loc='upper center', bbox_to_anchor=(0.5, 1.25), ncol=2)
axs[1].grid(axis='y', linestyle='--', linewidth=0.7)





# 第3个子图：VO Size vs Number (Blocks)
Mulchain_v_VO_BTC = [76.7972, 76.7978, 76.7981, 76.7982, 76.7983, 76.8079, 76.8127]

Mulchain_v_VO_ETH = [98.2340, 98.2346, 98.2349, 98.2351, 98.2351, 98.2447, 98.2495]

bar9 = [value - w for value, w in zip(x, widths_bar)]  # 左侧的柱状位置
bar10 = [value for value, w in zip(x, widths_bar)]  # 左侧的柱状位置

axs[2].bar(bar9, Mulchain_v_VO_BTC, color='#9CD1C8', width=widths_bar,
           label='MulChain$_VB$')
axs[2].bar(bar10, Mulchain_v_VO_ETH, color='#6BB7CA', width=widths_bar,
           label='MulChain$_VE$')

# 设置25个子图的坐标轴
axs[2].set_xlabel('Number (Blocks)\n(c) VO Size', fontsize=20)
axs[2].set_ylabel('VO Size (KB)', fontsize=20)
axs[2].set_xscale('log', base=2)  # 设置x轴为对数制度，底数为2

axs[2].set_xticks(x)  # 设置X轴制点

axs[2].set_xticklabels(x, fontsize=20)


axs[2].legend(fontsize=12, loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=2)
axs[2].grid(axis='y', linestyle='--', linewidth=0.7)

# 调整子图布局
plt.tight_layout()

# 保存图表
plt.savefig('../Figures/SimpleQ_all.pdf', dpi=360)

# 显示图表
plt.show()
