import hashlib
import json
import pickle
from datetime import datetime
from ipfshttpclient.client import Client

from solcx import compile_standard, install_solc, set_solc_version
from tqdm import tqdm
from Logger.Logger import log_time_range
from SQL_MiddleWare import SQLMiddleware, generate_random_times

block_sizes = [8, 16, 32, 64, 128, 256, 512]


def generate_text_hash(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def main():
    # 假设合约和 IPFS 客户端实例已被初始化
    try:
        ipfs_client = Client('/ip4/127.0.0.1/tcp/5001')  # 替换为你的 IPFS 节点地址
    except Exception as e:
        print(e)
        print("IPFS Connect failed, plz check if ipfs is configured correctly and turned on")
        ipfs_client = None
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

    # 逐步增加块的数量，从 256 到 16384

    with open('data_list.pkl', 'rb') as f:
        data_list = pickle.load(f)

    time_stamp_list = []
    for data in data_list:
        # 解析日期字符串为 datetime 对象
        dt_object = datetime.strptime(data['time_stamp'], '%Y-%m-%d %H:%M:%S')
        # 将 datetime 对象转换为日期字符串
        formatted_date = dt_object.strftime('%Y-%m-%d %H:%M:%S')
        # data['time_stamp'] = formatted_date
        time_stamp_list.append(formatted_date)

    min_time = min(time_stamp_list)
    max_time = max(time_stamp_list)
    print("min_time:", min_time)
    print("max_time:", max_time)

    # 验证是否成功读取
    print(f"Loaded {len(data_list)} items from data_list.pkl")
    with open("AAA_TIME_INDEX_COST_BTC" + str(datetime.now().strftime('%Y-%m-%d %H_%M_%S')), 'a+') as fw:
        for j in range(0, len(block_sizes)):
            block_size = block_sizes[j]
            print(f"----- Starting test for {block_size} blocks -----")
            fw.write(f"----- Starting test for {block_size} blocks -----")
            fw.write("\n")
            print(f"----- Starting insert query for {block_size} blocks -----")
            for i in tqdm(range(0 if j == 0 else block_sizes[j - 1], block_size)):
                text_hash = data_list[i]['hash']
                time_stamp = data_list[i]['time_stamp']
                image_path = "sample_image.jpg"  # 请替换为实际图片路径
                video_path = "sample_video.mp4"  # 请替换为实际视频路径
                insert_query = f"INSERT INTO multimodal_data (textHash, imageCID, videoCID, timestamp) VALUES ('{text_hash}', '{image_path}', '{video_path}', '{time_stamp}')"
                sql_middleware.parse_query(insert_query)

            print(f"----- Starting select query for {block_size} blocks -----")
            for _ in tqdm(range(0 if j == 0 else block_sizes[j - 1], block_size)):
                # 构建 SELECT 查询并调用 parse_query
                a, b = generate_random_times(min_time, max_time)
                select_query = f"SELECT * FROM multimodal_data WHERE timestamp BETWEEN '{a}' AND '{b}'"
                sql_middleware.parse_query(select_query)
            log_time_range(sql_middleware, fw, block_size)


if __name__ == "__main__":
    main()
