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
print("max_incre in query latency", max_incre)

Mulchain_v_VO_BTC = [635.9648, 903.9232, 1563.1016, 2953.8084, 5760.6786, 11409.6719, 22787.2088]
Mulchain_bh_VO_BTC = [164.3568, 142.9200, 132.2016, 126.8424, 124.1628, 122.8230, 122.1531]
Mulchain_v_VO_ETH = [657.4016, 936.0784, 1632.7712, 3095.8264, 6056.7724, 12006.8006, 23985.2363]
Mulchain_bh_VO_ETH = [164.3568, 142.9200, 132.2016, 126.8424, 124.1628, 122.8230, 122.1531]
max_VO_size_decre = 0.0
for i in range(len(Mulchain_v_VO_BTC)):
    max_VO_size_decre = max(abs(Mulchain_v_VO_BTC[i] - Mulchain_bh_VO_BTC[i])
                            / Mulchain_v_VO_BTC[i], max_VO_size_decre)
    max_VO_size_decre = max(abs(Mulchain_v_VO_ETH[i] - Mulchain_bh_VO_ETH[i])
                            / Mulchain_v_VO_ETH[i], max_VO_size_decre)
print("max_decre in VO Size", max_VO_size_decre)
