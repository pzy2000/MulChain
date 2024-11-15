import numpy as np
Mulchain_v_latency_BTC = [0.0888, 0.1165, 0.1896, 0.3443, 0.6559, 1.2873, 2.5559]
Mulchain_bt_latency_BTC = [0.0371, 0.0349, 0.0341, 0.0344, 0.0343, 0.0345, 0.0346]
Mulchain_bh_latency_BTC = [0.0335, 0.0330, 0.0322, 0.0328, 0.0329, 0.0327, 0.0333]
Mulchain_o_latency_BTC = [0.0335, 0.0330, 0.0322, 0.0328, 0.0329, 0.0327, 0.0333]

Mulchain_v_latency_ETH = [0.0950, 0.1206, 0.1930, 0.3505, 0.6709, 1.3139, 2.6067]
Mulchain_bt_latency_ETH = [0.0337, 0.0335, 0.0333, 0.0335, 0.0340, 0.0344, 0.0346]
Mulchain_bh_latency_ETH = [0.0324, 0.0333, 0.0325, 0.0326, 0.0327, 0.0330, 0.0333]
Mulchain_o_latency_ETH = [0.0324, 0.0333, 0.0325, 0.0326, 0.0327, 0.0330, 0.0333]

max_incre = 0.0
for i in range(len(Mulchain_v_latency_BTC)):
    max_incre = max(abs(Mulchain_bh_latency_BTC[i] - Mulchain_v_latency_BTC[i])
                    / Mulchain_v_latency_BTC[i], max_incre)
    max_incre = max(abs(Mulchain_bh_latency_ETH[i] - Mulchain_v_latency_ETH[i])
                    / Mulchain_v_latency_ETH[i], max_incre)
print("max_incre in query latency (btc vs eth)", max_incre)
print("==================================================")

Mulchain_v_VO_BTC = [635.9648, 903.9232, 1563.1016, 2953.8084, 5760.6786, 11409.6719, ]
Mulchain_bh_VO_BTC = [164.3568, 142.9200, 132.2016, 126.8424, 124.1628, 122.8230, ]
Mulchain_v_VO_ETH = [657.4016, 936.0784, 1632.7712, 3095.8264, 6056.7724, 12006.8006, ]
Mulchain_bh_VO_ETH = [164.3568, 142.9200, 132.2016, 126.8424, 124.1628, 122.8230, ]
max_VO_size_decre = 0.0
for i in range(len(Mulchain_v_VO_BTC)):
    max_VO_size_decre = max(abs(Mulchain_v_VO_BTC[i] - Mulchain_bh_VO_BTC[i])
                            / Mulchain_v_VO_BTC[i], max_VO_size_decre)
    max_VO_size_decre = max(abs(Mulchain_v_VO_ETH[i] - Mulchain_bh_VO_ETH[i])
                            / Mulchain_v_VO_ETH[i], max_VO_size_decre)
print("max_decre in VO Size (btc vs eth)", max_VO_size_decre)
print("====================================================")

for i in range(len(Mulchain_v_latency_BTC)):
    tmp_BTC = np.true_divide(Mulchain_v_latency_BTC, Mulchain_o_latency_BTC)
    avg_incre = np.average(tmp_BTC)

print("Latency average_incre", avg_incre)
print("=================================")

Mulchain_v_VO_BTC = [76.7972, 76.7978, 76.7981, 76.7982, 76.7983, 76.8079, 76.8127]
Mulchain_v_VO_ETH = [98.2340, 98.2346, 98.2349, 98.2351, 98.2351, 98.2447, 98.2495]
# 逐元素减法
Mulchain_minus_BTC = [eth - btc for btc, eth in zip(Mulchain_v_VO_BTC, Mulchain_v_VO_ETH)]

# 输出结果
for i in range(len(Mulchain_v_latency_BTC)):
    tmp_BTC = np.true_divide(Mulchain_minus_BTC, Mulchain_v_VO_ETH)
    vo_avg_incre = np.average(tmp_BTC)

print("VO Size average_incre in BTC vs ETH", vo_avg_incre)
print("==================================================")

Mulchain_v_VO_BTC = [76.7972, 76.7978, 76.7981, 76.7982, 76.7983, 76.8079, ]
Mulchain_v_VO_ETH = [98.2340, 98.2346, 98.2349, 98.2351, 98.2351, 98.2447, ]
Mulchain_t_VO_BTC = [122.9724, 131.0111, 129.3364, 132.6859, 129.8388, 132.6440, ]
Mulchain_t_VO_ETH = [784.8311, 1015.9459, 1211.2209, 1475.3281, 3246.8717, 5071.3371, ]

# 逐元素减法
Mulchain_minus_BTC = [t - v for t, v in zip(Mulchain_t_VO_BTC, Mulchain_v_VO_BTC)]
Mulchain_minus_ETH = [t - v for t, v in zip(Mulchain_t_VO_ETH, Mulchain_v_VO_ETH)]

# 输出结果
tmp_BTC = np.true_divide(Mulchain_minus_BTC, Mulchain_v_VO_BTC)
tmp_ETH = np.true_divide(Mulchain_minus_ETH, Mulchain_v_VO_ETH)
tmp_all = np.concatenate((tmp_BTC, tmp_ETH))
vo_avg_incre = np.average(tmp_BTC)
vo_avg_incre_ETH = np.average(tmp_ETH)
vo_avg_incre_all = np.average(tmp_all)

print("VO Size average_incre in BTC", vo_avg_incre)
print("VO Size average_incre in ETH", vo_avg_incre_ETH)
print("VO Size average_incre in ALL", vo_avg_incre_all)

Mulchain_v_latency_BTC = [0.3803, 0.5719, 1.0186, 1.9726, 3.9202, 7.8390, 15.8249]
Mulchain_Tr_latency_BTC = [0.0298, 0.0455, 0.0380, 0.0381, 0.0399, 0.0403, 0.0466]

Mulchain_v_latency_ETH = [0.5325, 0.7084, 1.1328, 2.0620, 4.0100, 7.9133, 16.1916]
Mulchain_Tr_latency_ETH = [0.2345, 0.2494, 0.2330, 0.2232, 0.3397, 0.4468, 0.8243]

Mulchain_minus_BTC = [t - v for t, v in zip(Mulchain_Tr_latency_BTC, Mulchain_v_latency_BTC)]
Mulchain_minus_ETH = [t - v for t, v in zip(Mulchain_Tr_latency_ETH, Mulchain_v_latency_ETH)]

# 输出结果
tmp_BTC = np.true_divide(Mulchain_minus_BTC, Mulchain_v_latency_BTC)
tmp_ETH = np.true_divide(Mulchain_minus_ETH, Mulchain_v_latency_ETH)
latency_avg_incre_BTC = np.average(tmp_BTC)
latency_max_incre_BTC = np.max(abs(tmp_BTC))
latency_avg_incre_ETH = np.average(tmp_ETH)
latency_max_incre_ETH = np.max(abs(tmp_ETH))

print("latency average_incre in BTC", latency_avg_incre_BTC)
print("latency average_incre in ETH", latency_avg_incre_ETH)

print("latency max_incre in BTC", latency_max_incre_BTC)
print("latency max_incre in ETH", latency_max_incre_ETH)

Mulchain_v_CPU_Time_BTC = [0.5347, 0.5273, 0.5204, 0.5178, 0.5157, 0.5148, 0.5145]
print("decline:", (0.5347 - 0.5145) / 0.5347)
