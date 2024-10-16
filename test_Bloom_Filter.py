import hashlib
import json
import random
import string
import ipfshttpclient
from pybloom_live import BloomFilter  # 导入 Bloom 过滤器
from solcx import compile_standard, install_solc, set_solc_version
from tqdm import tqdm
from SQL_MiddleWare import SQLMiddleware

# 安装并设置 Solidity 编译器版本
install_solc("0.8.20")
set_solc_version("0.8.20")

# 连接 Geth 本地测试链和 IPFS 节点
client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')  # 替换为你的 IPFS 节点地址
from global_w3 import w3

# 创建布隆过滤器来跟踪已存储的哈希，避免重复存储
bloom_filter = BloomFilter(capacity=50000000, error_rate=0.005)

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

# 保存编译后的代码
with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# 加载合约 ABI 和 Bytecode
bytecode = compiled_sol['contracts']['management_storage.sol']['MultiModalStorageManager']['evm']['bytecode']['object']
abi = compiled_sol['contracts']['management_storage.sol']['MultiModalStorageManager']['abi']
MultiModalStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# 部署合约
tx_hash = MultiModalStorage.constructor().transact()
# 手动生成新区块
w3.provider.make_request("evm_mine", [])
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
contract_instance = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

# 引入 SQL 中间件
sql_middleware = SQLMiddleware(contract_instance, client)

# 测试代码
insert_query = "INSERT INTO multimodal_data (textHash, imageCID, videoCID) VALUES ('sample_text_hash', 'sample_image.jpg', 'sample_video.mp4')"
print(sql_middleware.parse_query(insert_query))
print(sql_middleware.parse_query(insert_query))  # 再次插入相同的数据，应该被布隆过滤器检测为重复


# 随机生成大量的哈希值，并测试布隆过滤器的误报率
def random_hash():
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    return hashlib.sha256(random_string.encode('utf-8')).hexdigest()


false_positives = 0
total_tests = 0

for i in tqdm(range(50000000)):
    new_hash = random_hash()
    if new_hash in bloom_filter:
        false_positives += 1
    else:
        bloom_filter.add(new_hash)

    total_tests += 1

    if i % 50000 == 0 and i > 0:
        false_positive_rate = false_positives / total_tests
        print(f"Loop {i}, False Positive Rate: {false_positive_rate}")
