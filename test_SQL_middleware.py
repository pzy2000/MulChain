import json
import ipfshttpclient
from solcx import compile_standard, install_solc, set_solc_version
from SQL_MiddleWare import SQLMiddleware
from global_w3 import w3

# 安装并设置 Solidity 编译器版本
install_solc("0.8.20")
set_solc_version("0.8.20")

# 连接 Geth 本地测试链和 IPFS 节点
client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')  # 替换为你的 IPFS 节点地址


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
bytecode = compiled_sol['contracts']['management_storage.sol']['MultiModalStorageManager']['evm']['bytecode']['object']
abi = compiled_sol['contracts']['management_storage.sol']['MultiModalStorageManager']['abi']
MultiModalStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# 部署合约
tx_hash = MultiModalStorage.constructor().transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
contract_instance = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

# 引入 SQL 中间件
sql_middleware = SQLMiddleware(contract_instance, client)

# 测试 INSERT 操作
print("----- Testing INSERT operation -----")
insert_query = "INSERT INTO multimodal_data (textHash, imageCID, videoCID) VALUES ('sample_text_hash', 'sample_image.jpg', 'sample_video.mp4')"
print(sql_middleware.parse_query(insert_query))

# 测试 SELECT 操作
print("----- Testing SELECT operation -----")
select_query = "SELECT * FROM multimodal_data WHERE entry_id = 0"
result = sql_middleware.parse_query(select_query)
print(result)

print("----- Testing SELECT operation -----")
select_query = "SELECT * FROM multimodal_data WHERE entry_id = 0"
result = sql_middleware.parse_query(select_query)
print(result)

# 测试 UPDATE 操作
print("----- Testing UPDATE operation -----")
update_query = "UPDATE multimodal_data SET textHash = 'updated_text_hash', imageCID = 'updated_image.jpg', videoCID = 'updated_video.mp4' WHERE entry_id = 0"
print(sql_middleware.parse_query(update_query))

# 再次测试 SELECT 操作，查看更新后的数据
print("----- Testing SELECT after UPDATE -----")
result = sql_middleware.parse_query(select_query)
print(result)
