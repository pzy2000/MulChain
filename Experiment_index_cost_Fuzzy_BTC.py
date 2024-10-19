import hashlib
import json
import pickle
from datetime import datetime

import ipfshttpclient
from solcx import compile_standard, install_solc, set_solc_version
from tqdm import tqdm

from SQL_MiddleWare import SQLMiddleware, block_sizes, generate_random_date


def generate_text_hash(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


# print(random_date)

def main():
    # 假设合约和 IPFS 客户端实例已被初始化
    ipfs_client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')  # 替换为你的 IPFS 节点地址
    from global_w3 import w3

    # 安装并设置 Solidity 编译器版本
    install_solc("0.8.20")
    set_solc_version("0.8.20")

    # 加载并编译 Solidity 合约
    with open("contracts/management_storage.sol", "r", encoding="utf-8") as file:
        simple_nft_file = file.read()

    compiled_sol = compile_standard(
        {
            "language": "Solidity",
            "sources": {"management_storage.sol": {"content": simple_nft_file}},
            "settings": {
                "outputSelection": {
                    "*": {
                        "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
                    }
                }
            },
        },
        allow_paths=["."]
    )

    # 确保写入文件后关闭
    with open("compiled_code.json", "w") as file:
        json.dump(compiled_sol, file)

    # 加载合约 ABI 和 Bytecode
    bytecode = compiled_sol['contracts']['management_storage.sol']['MultiModalStorageManager']['evm']['bytecode'][
        'object']
    abi = compiled_sol['contracts']['management_storage.sol']['MultiModalStorageManager']['abi']
    MultiModalStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

    # 部署合约
    tx_hash = MultiModalStorage.constructor().transact()
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    contract_instance = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
    sql_middleware = SQLMiddleware(contract_instance, ipfs_client)

    with open('data_list.pkl', 'rb') as f:
        data_list = pickle.load(f)
    time_stamp_list = []
    for data in data_list:
        time_stamp_list.append(data['time_stamp'])
    min_time = min(time_stamp_list)
    max_time = max(time_stamp_list)
    min_time = datetime.strptime(min_time, '%Y-%m-%d %H:%M:%S')
    max_time = datetime.strptime(max_time, '%Y-%m-%d %H:%M:%S')
    print("min_time:", min_time)
    print("max_time:", max_time)
    # 验证是否成功读取
    print(f"Loaded {len(data_list)} items from data_list.pkl")
    with open("AAA_Fuzzy_INDEX_COST_BTC" + str(datetime.now().strftime('%Y-%m-%d %H_%M_%S')), 'a+') as fw:
        for j in range(0, len(block_sizes)):
            block_size = block_sizes[j]
            print(f"----- Starting test for {block_size} blocks -----")
            fw.write(f"----- Starting test for {block_size} blocks -----")
            fw.write("\n")
            for i in tqdm(range(0 if j == 0 else block_sizes[j - 1], block_size)):
                text_hash = data_list[i]['hash']
                time_stamp = data_list[i]['time_stamp']
                image_path = "sample_image.jpg"  # 请替换为实际图片路径
                video_path = "sample_video.mp4"  # 请替换为实际视频路径
                insert_query = f"INSERT INTO multimodal_data (textHash, imageCID, videoCID, timestamp) VALUES ('{text_hash}', '{image_path}', '{video_path}', '{time_stamp}')"
                sql_middleware.parse_query(insert_query)
                # 构建 SELECT 查询并调用 parse_query

            for _ in tqdm(range(0 if j == 0 else block_sizes[j - 1], block_size)):
                # 构建 SELECT 查询并调用 parse_query
                # 定义最小和最大时间
                # 生成随机日期
                random_date = generate_random_date(min_time, max_time)
                random_date += '%'
                select_query = f"SELECT * FROM multimodal_data WHERE time_stamp LIKE '{random_date}'"
                result = sql_middleware.parse_query(select_query)
                if result:
                    print(result)

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
                f"Select ADDER latency for {block_size} blocks: {sum(sql_middleware.select_adder_latency) / len(sql_middleware.select_adder_latency):.4f} seconds")
            fw.write(
                f"Select ADDER latency for {block_size} blocks: {sum(sql_middleware.select_adder_latency) / len(sql_middleware.select_adder_latency):.4f} seconds")
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


if __name__ == "__main__":
    main()
