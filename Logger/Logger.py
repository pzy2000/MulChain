from global_w3 import gas_per_kb

def log_GAS(sql_middleware, fw, block_size):
    # 输出统计数据
    avg_MulChain_v_index_build_time = sum(sql_middleware.index_building_times) / len(
        sql_middleware.index_building_times)
    avg_MulChain_o_index_build_time = (sum(sql_middleware.MulChain_o_index_building_times) /
                                       len(sql_middleware.MulChain_o_index_building_times))
    avg_MulChain_v_select_latency = sum(sql_middleware.select_adder_latency) / len(sql_middleware.select_adder_latency)
    avg_MulChain_o_select_latency = sum(sql_middleware.select_MulChain_o_latency) / len(
        sql_middleware.select_MulChain_o_latency)
    avg_MulChain_BT_select_latency = sum(sql_middleware.select_latency) / len(sql_middleware.select_latency)
    avg_MulChain_BH_select_latency = sum(sql_middleware.select_BHash_latency) / len(
        sql_middleware.select_BHash_latency)

    print(f"MulChain_v Insert time for {block_size} blocks: {avg_MulChain_v_index_build_time:.4f} seconds")
    fw.write(
        f"MulChain_v Insert time for {block_size} blocks: {avg_MulChain_v_index_build_time:.4f} seconds")
    fw.write("\n")

    print(
        f"MulChain_o Insert time for {block_size} blocks: {avg_MulChain_o_index_build_time:.4f} seconds")
    fw.write(
        f"MulChain_o Insert time for {block_size} blocks: {avg_MulChain_o_index_build_time:.4f} seconds")
    fw.write("\n")

    print(
        f"MulChain_v Select latency for {block_size} blocks: {avg_MulChain_v_select_latency:.4f} seconds")
    fw.write(
        f"MulChain_v Select latency for {block_size} blocks: {avg_MulChain_v_select_latency:.4f} seconds")
    fw.write("\n")

    print(
        f"MulChain_Bt Select latency for {block_size} blocks: {avg_MulChain_BT_select_latency:.4f} seconds")
    fw.write(
        f"MulChain_Bt Select latency for {block_size} blocks: {avg_MulChain_BT_select_latency:.4f} seconds")
    fw.write("\n")

    print(
        f"MulChain_BH Select latency for {block_size} blocks: {avg_MulChain_BH_select_latency:.4f} seconds")
    fw.write(
        f"MulChain_BH Select latency for {block_size} blocks: {avg_MulChain_BH_select_latency:.4f} seconds")
    fw.write("\n")

    print(
        f"MulChain_o Select latency for {block_size} blocks: {avg_MulChain_o_select_latency:.4f} seconds")
    fw.write(
        f"MulChain_o Select latency for {block_size} blocks: {avg_MulChain_o_select_latency:.4f} seconds")
    fw.write("\n")

    print(
        f"MulChain_v_vo_size for {block_size} blocks: {sum(sql_middleware.vo_adder_size_kb) / len(sql_middleware.vo_adder_size_kb):.4f} KB")
    fw.write(
        f"MulChain_v_vo_size for {block_size} blocks: {sum(sql_middleware.vo_adder_size_kb) / len(sql_middleware.vo_adder_size_kb):.4f} KB")
    fw.write("\n")

    print(
        f"MulChain_Bt_vo_size for {block_size} blocks: {sum(sql_middleware.vo_btree_size_kb) / len(sql_middleware.vo_btree_size_kb):.4f} KB")
    fw.write(
        f"MulChain_Bt_vo_size for {block_size} blocks: {sum(sql_middleware.vo_btree_size_kb) / len(sql_middleware.vo_btree_size_kb):.4f} KB")
    fw.write("\n")

    print(
        f"MulChain_BH_vo_size for {block_size} blocks: {sum(sql_middleware.vo_bhashtree_size_kb) / len(sql_middleware.vo_bhashtree_size_kb):.4f} MB")
    fw.write(
        f"MulChain_BH_vo_size for {block_size} blocks: {sum(sql_middleware.vo_bhashtree_size_kb) / len(sql_middleware.vo_bhashtree_size_kb):.4f} MB")
    fw.write("\n")

    print(
        f"Adder_gas(Avg) for {block_size} blocks: {sum(sql_middleware.vo_adder_size_kb) * gas_per_kb / len(sql_middleware.vo_adder_size_kb):.4f}")
    fw.write(
        f"Adder_gas(Avg) for {block_size} blocks: {sum(sql_middleware.vo_adder_size_kb) * gas_per_kb / len(sql_middleware.vo_adder_size_kb):.4f}")
    fw.write("\n")

    print(
        f"btree_gas(Avg) for {block_size} blocks: {sum(sql_middleware.vo_btree_size_kb) * gas_per_kb / len(sql_middleware.vo_btree_size_kb):.4f} ")
    fw.write(
        f"btree_gas(Avg) for {block_size} blocks: {sum(sql_middleware.vo_btree_size_kb) * gas_per_kb / len(sql_middleware.vo_btree_size_kb):.4f} ")
    fw.write("\n")

    print(
        f"bhashtree_gas(Avg) for {block_size} blocks: {sum(sql_middleware.vo_bhashtree_size_kb) * gas_per_kb / len(sql_middleware.vo_bhashtree_size_kb):.4f}")
    fw.write(
        f"bhashtree_gas(Avg) for {block_size} blocks: {sum(sql_middleware.vo_bhashtree_size_kb) * gas_per_kb / len(sql_middleware.vo_bhashtree_size_kb):.4f}")
    fw.write("\n")


def log_time_range(sql_middleware, fw, block_size):
    # 输出统计数据
    avg_MulChain_v_index_build_time = sum(sql_middleware.index_building_times) / len(
        sql_middleware.index_building_times)
    avg_MulChain_o_index_build_time = (sum(sql_middleware.MulChain_o_index_building_times) /
                                       len(sql_middleware.MulChain_o_index_building_times))
    avg_MulChain_v_select_latency = sum(sql_middleware.select_adder_latency) / len(sql_middleware.select_adder_latency)
    avg_MulChain_o_select_latency = sum(sql_middleware.select_MulChain_o_latency) / len(
        sql_middleware.select_MulChain_o_latency)
    avg_MulChain_BT_select_latency = sum(sql_middleware.select_latency) / len(sql_middleware.select_latency)
    avg_MulChain_BH_select_latency = sum(sql_middleware.select_BHash_latency) / len(
        sql_middleware.select_BHash_latency)

    print(f"MulChain_v Insert time for {block_size} blocks: {avg_MulChain_v_index_build_time:.4f} seconds")
    fw.write(
        f"MulChain_v Insert time for {block_size} blocks: {avg_MulChain_v_index_build_time:.4f} seconds")
    fw.write("\n")

    print(
        f"MulChain_o Insert time for {block_size} blocks: {avg_MulChain_o_index_build_time:.4f} seconds")
    fw.write(
        f"MulChain_o Insert time for {block_size} blocks: {avg_MulChain_o_index_build_time:.4f} seconds")
    fw.write("\n")

    print(
        f"MulChain_v Select latency for {block_size} blocks: {avg_MulChain_v_select_latency:.4f} seconds")
    fw.write(
        f"MulChain_v Select latency for {block_size} blocks: {avg_MulChain_v_select_latency:.4f} seconds")
    fw.write("\n")

    print(
        f"MulChain_Bt Select latency for {block_size} blocks: {avg_MulChain_BT_select_latency:.4f} seconds")
    fw.write(
        f"MulChain_Bt Select latency for {block_size} blocks: {avg_MulChain_BT_select_latency:.4f} seconds")
    fw.write("\n")

    print(
        f"MulChain_BH Select latency for {block_size} blocks: {avg_MulChain_BH_select_latency:.4f} seconds")
    fw.write(
        f"MulChain_BH Select latency for {block_size} blocks: {avg_MulChain_BH_select_latency:.4f} seconds")
    fw.write("\n")

    print(
        f"MulChain_o Select latency for {block_size} blocks: {avg_MulChain_o_select_latency:.4f} seconds")
    fw.write(
        f"MulChain_o Select latency for {block_size} blocks: {avg_MulChain_o_select_latency:.4f} seconds")
    fw.write("\n")

    print(
        f"MulChain_v_vo_size for {block_size} blocks: {sum(sql_middleware.vo_adder_size_kb) / len(sql_middleware.vo_adder_size_kb):.4f} KB")
    fw.write(
        f"MulChain_v_vo_size for {block_size} blocks: {sum(sql_middleware.vo_adder_size_kb) / len(sql_middleware.vo_adder_size_kb):.4f} KB")
    fw.write("\n")

    print(
        f"MulChain_Bt_vo_size for {block_size} blocks: {sum(sql_middleware.vo_btree_size_kb) / len(sql_middleware.vo_btree_size_kb):.4f} KB")
    fw.write(
        f"MulChain_Bt_vo_size for {block_size} blocks: {sum(sql_middleware.vo_btree_size_kb) / len(sql_middleware.vo_btree_size_kb):.4f} KB")
    fw.write("\n")

    print(
        f"MulChain_BH_vo_size for {block_size} blocks: {sum(sql_middleware.vo_bhashtree_size_kb) / len(sql_middleware.vo_bhashtree_size_kb):.4f} MB")
    fw.write(
        f"MulChain_BH_vo_size for {block_size} blocks: {sum(sql_middleware.vo_bhashtree_size_kb) / len(sql_middleware.vo_bhashtree_size_kb):.4f} MB")
    fw.write("\n")

    print(
        f"Adder_gas(Avg) for {block_size} blocks: {sum(sql_middleware.vo_adder_size_kb) * gas_per_kb / len(sql_middleware.vo_adder_size_kb):.4f}")
    fw.write(
        f"Adder_gas(Avg) for {block_size} blocks: {sum(sql_middleware.vo_adder_size_kb) * gas_per_kb / len(sql_middleware.vo_adder_size_kb):.4f}")
    fw.write("\n")

    print(
        f"btree_gas(Avg) for {block_size} blocks: {sum(sql_middleware.vo_btree_size_kb) * gas_per_kb / len(sql_middleware.vo_btree_size_kb):.4f} ")
    fw.write(
        f"btree_gas(Avg) for {block_size} blocks: {sum(sql_middleware.vo_btree_size_kb) * gas_per_kb / len(sql_middleware.vo_btree_size_kb):.4f} ")
    fw.write("\n")

    print(
        f"bhashtree_gas(Avg) for {block_size} blocks: {sum(sql_middleware.vo_bhashtree_size_kb) * gas_per_kb / len(sql_middleware.vo_bhashtree_size_kb):.4f}")
    fw.write(
        f"bhashtree_gas(Avg) for {block_size} blocks: {sum(sql_middleware.vo_bhashtree_size_kb) * gas_per_kb / len(sql_middleware.vo_bhashtree_size_kb):.4f}")
    fw.write("\n")


def log_fuzzy(sql_middleware, fw, block_size):
    # 输出统计数据
    avg_MulChain_v_index_build_time = sum(sql_middleware.index_building_times) / len(
        sql_middleware.index_building_times)
    avg_MulChain_o_index_build_time = (sum(sql_middleware.MulChain_o_index_building_times) /
                                       len(sql_middleware.MulChain_o_index_building_times))
    avg_MulChain_v_select_latency = sum(sql_middleware.select_adder_latency) / len(sql_middleware.select_adder_latency)
    avg_MulChain_o_select_latency = sum(sql_middleware.select_MulChain_o_latency) / len(
        sql_middleware.select_MulChain_o_latency)
    avg_MulChain_Tr_select_latency = sum(sql_middleware.select_Trie_latency) / len(
        sql_middleware.select_Trie_latency)

    print(f"MulChain_v Insert time for {block_size} blocks: {avg_MulChain_v_index_build_time:.4f} seconds")
    fw.write(
        f"MulChain_v Insert time for {block_size} blocks: {avg_MulChain_v_index_build_time:.4f} seconds")
    fw.write("\n")
    print(
        f"MulChain_o Insert time for {block_size} blocks: {avg_MulChain_o_index_build_time:.4f} seconds")
    fw.write(
        f"MulChain_o Insert time for {block_size} blocks: {avg_MulChain_o_index_build_time:.4f} seconds")
    fw.write("\n")

    print(
        f"MulChain_v Select latency for {block_size} blocks: {avg_MulChain_v_select_latency:.4f} seconds")
    fw.write(
        f"MulChain_v Select latency for {block_size} blocks: {avg_MulChain_v_select_latency:.4f} seconds")
    fw.write("\n")

    print(
        f"MulChain_Tr Select latency for {block_size} blocks: {avg_MulChain_Tr_select_latency:.4f} seconds")
    fw.write(
        f"MulChain_Tr Select latency for {block_size} blocks: {avg_MulChain_Tr_select_latency:.4f} seconds")
    fw.write("\n")

    print(
        f"MulChain_o Select latency for {block_size} blocks: {avg_MulChain_o_select_latency:.4f} seconds")
    fw.write(
        f"MulChain_o Select latency for {block_size} blocks: {avg_MulChain_o_select_latency:.4f} seconds")
    fw.write("\n")

    print(
        f"MulChain_v_vo_size for {block_size} blocks: {sum(sql_middleware.vo_adder_size_kb) / len(sql_middleware.vo_adder_size_kb):.4f} KB")
    fw.write(
        f"MulChain_v_vo_size for {block_size} blocks: {sum(sql_middleware.vo_adder_size_kb) / len(sql_middleware.vo_adder_size_kb):.4f} KB")
    fw.write("\n")

    print(
        f"MulChain_Trie_vo_size for {block_size} blocks: {sum(sql_middleware.vo_trie_size_kb) / len(sql_middleware.vo_trie_size_kb):.4f} MB")
    fw.write(
        f"MulChain_Trie_vo_size for {block_size} blocks: {sum(sql_middleware.vo_trie_size_kb) / len(sql_middleware.vo_trie_size_kb):.4f} MB")
    fw.write("\n")

    print(
        f"Adder_gas(Avg) for {block_size} blocks: {sum(sql_middleware.vo_adder_size_kb) * gas_per_kb / len(sql_middleware.vo_adder_size_kb):.4f}")
    fw.write(
        f"Adder_gas(Avg) for {block_size} blocks: {sum(sql_middleware.vo_adder_size_kb) * gas_per_kb / len(sql_middleware.vo_adder_size_kb):.4f}")
    fw.write("\n")

    print(
        f"Trie_gas(Avg) for {block_size} blocks: {sum(sql_middleware.vo_trie_size_kb) * gas_per_kb / len(sql_middleware.vo_trie_size_kb):.4f} ")
    fw.write(
        f"Trie_gas(Avg) for {block_size} blocks: {sum(sql_middleware.vo_trie_size_kb) * gas_per_kb / len(sql_middleware.vo_trie_size_kb):.4f} ")
    fw.write("\n")


def log_simple(sql_middleware, fw, block_size):
    # 输出统计数据
    avg_MulChain_v_index_build_time = sum(sql_middleware.index_building_times) / len(
        sql_middleware.index_building_times)
    avg_MulChain_o_index_build_time = (sum(sql_middleware.MulChain_o_index_building_times) /
                                       len(sql_middleware.MulChain_o_index_building_times))
    avg_MulChain_v_select_latency = sum(sql_middleware.select_latency) / len(sql_middleware.select_latency)
    avg_MulChain_o_select_latency = sum(sql_middleware.select_MulChain_o_latency) / len(
        sql_middleware.select_MulChain_o_latency)

    print(f"MulChain_v Insert time for {block_size} blocks: {avg_MulChain_v_index_build_time:.4f} seconds")
    fw.write(
        f"MulChain_v Insert time for {block_size} blocks: {avg_MulChain_v_index_build_time:.4f} seconds")
    fw.write("\n")

    print(
        f"MulChain_o Insert time for {block_size} blocks: {avg_MulChain_o_index_build_time:.4f} seconds")
    fw.write(
        f"MulChain_o Insert time for {block_size} blocks: {avg_MulChain_o_index_build_time:.4f} seconds")
    fw.write("\n")

    print(
        f"MulChain_v Select latency for {block_size} blocks: {avg_MulChain_v_select_latency:.4f} seconds")
    fw.write(
        f"MulChain_v Select latency for {block_size} blocks: {avg_MulChain_v_select_latency:.4f} seconds")
    fw.write("\n")

    print(
        f"MulChain_o Select latency for {block_size} blocks: {avg_MulChain_o_select_latency:.4f} seconds")
    fw.write(
        f"MulChain_o Select latency for {block_size} blocks: {avg_MulChain_o_select_latency:.4f} seconds")
    fw.write("\n")

    print(
        f"MulChain_v_vo_size for {block_size} blocks: {sum(sql_middleware.vo_adder_size_kb) / len(sql_middleware.vo_adder_size_kb) :.4f} KB")
    fw.write(
        f"MulChain_v_vo_size for {block_size} blocks: {sum(sql_middleware.vo_adder_size_kb) / len(sql_middleware.vo_adder_size_kb) :.4f} KB")
    fw.write("\n")

    print(
        f"MulChain_v_gas(Avg) for {block_size} blocks: {sum(sql_middleware.vo_adder_size_kb) * gas_per_kb / len(sql_middleware.vo_adder_size_kb):.4f}")
    fw.write(
        f"MulChain_v_gas(Avg) for {block_size} blocks: {sum(sql_middleware.vo_adder_size_kb) * gas_per_kb / len(sql_middleware.vo_adder_size_kb):.4f}")
    fw.write("\n")
