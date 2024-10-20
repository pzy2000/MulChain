from global_w3 import gas_per_kb


def log_time_range(sql_middleware, fw, block_size):
    # 输出统计数据
    avg_index_build_time = sum(sql_middleware.index_building_times) / len(sql_middleware.index_building_times)
    avg_block_generation_time = sum(sql_middleware.block_generation_times) / len(
        sql_middleware.block_generation_times)
    avg_index_storage_cost = sum(sql_middleware.index_storage_costs) / len(sql_middleware.index_storage_costs)

    print(f"Index build time for {block_size} blocks: {sum(sql_middleware.index_building_times):.4f} seconds")
    fw.write(
        f"Index build time for {block_size} blocks: {sum(sql_middleware.index_building_times):.4f} seconds")
    fw.write("\n")

    print(
        f"On-Chain Index build time for {block_size} blocks: {sum(sql_middleware.on_chain_index_building_times):.4f} seconds")
    fw.write(
        f"On-Chain Index build time for {block_size} blocks: {sum(sql_middleware.on_chain_index_building_times):.4f} seconds")
    fw.write("\n")

    print(
        f"Block generation time for {block_size} blocks: {sum(sql_middleware.block_generation_times):.4f} seconds")
    fw.write(
        f"Block generation time for {block_size} blocks: {sum(sql_middleware.block_generation_times):.4f} seconds")
    fw.write("\n")

    print(
        f"Index storage cost for {block_size} blocks: {sum(sql_middleware.index_storage_costs) / 1024:.8f} MB")
    fw.write(
        f"Index storage cost for {block_size} blocks: {sum(sql_middleware.index_storage_costs) / 1024:.8f} MB")
    fw.write("\n")

    print(
        f"vo_adder_size for {block_size} blocks: {sum(sql_middleware.vo_adder_size_kb) / 1024:.8f} MB")
    fw.write(
        f"vo_adder_size for {block_size} blocks: {sum(sql_middleware.vo_adder_size_kb) / 1024:.8f} MB")
    fw.write("\n")

    print(
        f"vo_btree_size for {block_size} blocks: {sum(sql_middleware.vo_btree_size_kb) / 1024:.8f} MB")
    fw.write(
        f"vo_btree_size for {block_size} blocks: {sum(sql_middleware.vo_btree_size_kb) / 1024:.8f} MB")
    fw.write("\n")

    print(
        f"vo_bhashtree_size for {block_size} blocks: {sum(sql_middleware.vo_bhashtree_size_kb) / 1024:.8f} MB")
    fw.write(
        f"vo_bhashtree_size for {block_size} blocks: {sum(sql_middleware.vo_bhashtree_size_kb) / 1024:.8f} MB")
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

    print(
        f"Select Btree latency for {block_size} blocks: {sum(sql_middleware.select_latency) / len(sql_middleware.select_latency):.4f} seconds")
    fw.write(
        f"Select Btree latency for {block_size} blocks: {sum(sql_middleware.select_latency) / len(sql_middleware.select_latency):.4f} seconds")
    fw.write("\n")

    print(
        f"Select ADDER latency for {block_size} blocks: {sum(sql_middleware.select_adder_latency) / len(sql_middleware.select_adder_latency):.4f} seconds")
    fw.write(
        f"Select ADDER latency for {block_size} blocks: {sum(sql_middleware.select_adder_latency) / len(sql_middleware.select_adder_latency):.4f} seconds")
    fw.write("\n")

    print(
        f"Select BHashTree latency for {block_size} blocks: {sum(sql_middleware.select_BHash_latency) / len(sql_middleware.select_BHash_latency):.4f} seconds")
    fw.write(
        f"Select BHashTree latency for {block_size} blocks: {sum(sql_middleware.select_BHash_latency) / len(sql_middleware.select_BHash_latency):.4f} seconds")
    fw.write("\n")

    print(
        f"On-chain Select latency for {block_size} blocks: {sum(sql_middleware.select_on_chain_latency) / len(sql_middleware.select_on_chain_latency):.4f} seconds")
    fw.write(
        f"On-chain Select latency for {block_size} blocks: {sum(sql_middleware.select_on_chain_latency) / len(sql_middleware.select_on_chain_latency):.4f} seconds")
    fw.write("\n")

    print(f"avg Index build time for {block_size} blocks: {avg_index_build_time:.4f} seconds")
    fw.write(f"avg Index build time for {block_size} blocks: {avg_index_build_time:.4f} seconds")
    fw.write("\n")

    print(
        f"avg On-Chain Index build time for {block_size} blocks: {sum(sql_middleware.on_chain_index_building_times) / len(sql_middleware.on_chain_index_building_times):.4f} seconds")
    fw.write(
        f"avg On-Chain Index build time for {block_size} blocks: {sum(sql_middleware.on_chain_index_building_times) / len(sql_middleware.on_chain_index_building_times):.4f} seconds")
    fw.write("\n")

    # print(
    #     f"avg Block generation time for {block_size} blocks: {sum(sql_middleware.block_generation_times) / len(sql_middleware.block_generation_times):.6f} seconds")
    print(f"avg Block generation time for {block_size} blocks: {avg_block_generation_time:.6f} seconds")
    fw.write(f"avg Block generation time for {block_size} blocks: {avg_block_generation_time:.6f} seconds")
    fw.write("\n")

    # print(
    # f"avg Index storage cost for {block_size} blocks: {sum(sql_middleware.index_storage_costs) / 1024 / len(sql_middleware.index_storage_costs):.8f} MB")
    print(f"avg Index storage cost for {block_size} blocks: {avg_index_storage_cost / 1024:.8f} MB")
    fw.write(f"avg Index storage cost for {block_size} blocks: {avg_index_storage_cost / 1024:.8f} MB")
    fw.write("\n")


def log_fuzzy(sql_middleware, fw, block_size):
    # 输出统计数据
    avg_index_build_time = sum(sql_middleware.index_building_times) / len(sql_middleware.index_building_times)
    avg_block_generation_time = sum(sql_middleware.block_generation_times) / len(
        sql_middleware.block_generation_times)
    avg_index_storage_cost = sum(sql_middleware.index_storage_costs) / len(sql_middleware.index_storage_costs)

    print(f"Index build time for {block_size} blocks: {sum(sql_middleware.index_building_times):.4f} seconds")
    fw.write(
        f"Index build time for {block_size} blocks: {sum(sql_middleware.index_building_times):.4f} seconds")
    fw.write("\n")

    print(
        f"On-Chain Index build time for {block_size} blocks: {sum(sql_middleware.on_chain_index_building_times):.4f} seconds")
    fw.write(
        f"On-Chain Index build time for {block_size} blocks: {sum(sql_middleware.on_chain_index_building_times):.4f} seconds")
    fw.write("\n")

    print(
        f"Block generation time for {block_size} blocks: {sum(sql_middleware.block_generation_times):.4f} seconds")
    fw.write(
        f"Block generation time for {block_size} blocks: {sum(sql_middleware.block_generation_times):.4f} seconds")
    fw.write("\n")

    print(
        f"Index storage cost for {block_size} blocks: {sum(sql_middleware.index_storage_costs) / 1024:.8f} MB")
    fw.write(
        f"Index storage cost for {block_size} blocks: {sum(sql_middleware.index_storage_costs) / 1024:.8f} MB")
    fw.write("\n")

    print(
        f"vo_adder_size for {block_size} blocks: {sum(sql_middleware.vo_adder_size_kb) / 1024:.8f} MB")
    fw.write(
        f"vo_adder_size for {block_size} blocks: {sum(sql_middleware.vo_adder_size_kb) / 1024:.8f} MB")
    fw.write("\n")

    print(
        f"vo_Trie_size for {block_size} blocks: {sum(sql_middleware.vo_trie_size_kb) / 1024:.8f} MB")
    fw.write(
        f"vo_Trie_size for {block_size} blocks: {sum(sql_middleware.vo_trie_size_kb) / 1024:.8f} MB")
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


    print(
        f"Select ADDER latency for {block_size} blocks: {sum(sql_middleware.select_adder_latency) / len(sql_middleware.select_adder_latency):.4f} seconds")
    fw.write(
        f"Select ADDER latency for {block_size} blocks: {sum(sql_middleware.select_adder_latency) / len(sql_middleware.select_adder_latency):.4f} seconds")
    fw.write("\n")

    print(
        f"Select Trie latency for {block_size} blocks: {sum(sql_middleware.select_Trie_latency) / len(sql_middleware.select_Trie_latency):.4f} seconds")
    fw.write(
        f"Select Trie latency for {block_size} blocks: {sum(sql_middleware.select_Trie_latency) / len(sql_middleware.select_Trie_latency):.4f} seconds")
    fw.write("\n")

    print(
        f"On-chain Select latency for {block_size} blocks: {sum(sql_middleware.select_on_chain_latency) / len(sql_middleware.select_on_chain_latency):.4f} seconds")
    fw.write(
        f"On-chain Select latency for {block_size} blocks: {sum(sql_middleware.select_on_chain_latency) / len(sql_middleware.select_on_chain_latency):.4f} seconds")
    fw.write("\n")

    print(f"avg Index build time for {block_size} blocks: {avg_index_build_time:.4f} seconds")
    fw.write(f"avg Index build time for {block_size} blocks: {avg_index_build_time:.4f} seconds")
    fw.write("\n")

    print(
        f"avg On-Chain Index build time for {block_size} blocks: {sum(sql_middleware.on_chain_index_building_times) / len(sql_middleware.on_chain_index_building_times):.4f} seconds")
    fw.write(
        f"avg On-Chain Index build time for {block_size} blocks: {sum(sql_middleware.on_chain_index_building_times) / len(sql_middleware.on_chain_index_building_times):.4f} seconds")
    fw.write("\n")

    print(f"avg Block generation time for {block_size} blocks: {avg_block_generation_time:.6f} seconds")
    fw.write(f"avg Block generation time for {block_size} blocks: {avg_block_generation_time:.6f} seconds")
    fw.write("\n")

    print(f"avg Index storage cost for {block_size} blocks: {avg_index_storage_cost / 1024:.8f} MB")
    fw.write(f"avg Index storage cost for {block_size} blocks: {avg_index_storage_cost / 1024:.8f} MB")
    fw.write("\n")


def log_simple(sql_middleware, fw, block_size):
    # 输出统计数据
    avg_index_build_time = sum(sql_middleware.index_building_times) / len(sql_middleware.index_building_times)
    avg_block_generation_time = sum(sql_middleware.block_generation_times) / len(
        sql_middleware.block_generation_times)
    avg_index_storage_cost = sum(sql_middleware.index_storage_costs) / len(sql_middleware.index_storage_costs)

    print(f"vChain+ Index build time for {block_size} blocks: {sum(sql_middleware.index_building_times):.4f} seconds")
    fw.write(
        f"vChain+ Index build time for {block_size} blocks: {sum(sql_middleware.index_building_times):.4f} seconds")
    fw.write("\n")

    print(
        f"On-Chain Index build time for {block_size} blocks: {sum(sql_middleware.on_chain_index_building_times):.4f} seconds")
    fw.write(
        f"On-Chain Index build time for {block_size} blocks: {sum(sql_middleware.on_chain_index_building_times):.4f} seconds")
    fw.write("\n")

    print(
        f"Block generation time for {block_size} blocks: {sum(sql_middleware.block_generation_times):.4f} seconds")
    fw.write(
        f"Block generation time for {block_size} blocks: {sum(sql_middleware.block_generation_times):.4f} seconds")
    fw.write("\n")

    print(
        f"Index storage cost for {block_size} blocks: {sum(sql_middleware.index_storage_costs) / 1024:.8f} MB")
    fw.write(
        f"Index storage cost for {block_size} blocks: {sum(sql_middleware.index_storage_costs) / 1024:.8f} MB")
    fw.write("\n")

    print(
        f"vChain+ Select latency for {block_size} blocks: {sum(sql_middleware.select_latency) / len(sql_middleware.select_latency):.4f} seconds")
    fw.write(
        f"vChain+ Select latency for {block_size} blocks: {sum(sql_middleware.select_latency) / len(sql_middleware.select_latency):.4f} seconds")
    fw.write("\n")

    print(
        f"On-chain Select latency for{block_size} blocks: {sum(sql_middleware.select_on_chain_latency) / len(sql_middleware.select_on_chain_latency):.4f} seconds")
    fw.write(
        f"On-chain Select latency for{block_size} blocks: {sum(sql_middleware.select_on_chain_latency) / len(sql_middleware.select_on_chain_latency):.4f} seconds")
    fw.write("\n")

    # print(
    #     f"avg Index build time for {block_size} blocks: {sum(sql_middleware.index_building_times) / len(sql_middleware.index_building_times):.4f} seconds")
    print(f"avg Index build time for {block_size} blocks: {avg_index_build_time:.4f} seconds")
    fw.write(f"avg Index build time for {block_size} blocks: {avg_index_build_time:.4f} seconds")
    fw.write("\n")

    print(
        f"avg On-Chain Index build time for {block_size} blocks: {sum(sql_middleware.on_chain_index_building_times) / len(sql_middleware.on_chain_index_building_times):.4f} seconds")
    fw.write(
        f"avg On-Chain Index build time for {block_size} blocks: {sum(sql_middleware.on_chain_index_building_times) / len(sql_middleware.on_chain_index_building_times):.4f} seconds")
    fw.write("\n")

    # print(
    #     f"avg Block generation time for {block_size} blocks: {sum(sql_middleware.block_generation_times) / len(sql_middleware.block_generation_times):.6f} seconds")
    print(f"avg Block generation time for {block_size} blocks: {avg_block_generation_time:.6f} seconds")
    fw.write(f"avg Block generation time for {block_size} blocks: {avg_block_generation_time:.6f} seconds")
    fw.write("\n")

    # print(
    # f"avg Index storage cost for {block_size} blocks: {sum(sql_middleware.index_storage_costs) / 1024 / len(sql_middleware.index_storage_costs):.8f} MB")
    print(f"avg Index storage cost for {block_size} blocks: {avg_index_storage_cost / 1024:.8f} MB")
    fw.write(f"avg Index storage cost for {block_size} blocks: {avg_index_storage_cost / 1024:.8f} MB")
    fw.write("\n")
