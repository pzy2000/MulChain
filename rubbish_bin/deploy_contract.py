import hashlib
import json
import ipfshttpclient
from solcx import compile_standard, install_solc, set_solc_version
from web3 import Web3
install_solc("0.8.20")
set_solc_version("0.8.20")
with open("../contracts/management_storage.sol", "r", encoding="utf-8") as file:
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

with open("../compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)
client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')
assert client, "IPFS node connection failed"
w3 = Web3(Web3.EthereumTesterProvider())
# 部署智能合约
bytecode = compiled_sol['contracts']['management_storage.sol']['MultiModalStorageManager']['evm']['bytecode']['object']
# print(f"Bytecode: {bytecode}")
abi = compiled_sol['contracts']['management_storage.sol']['MultiModalStorageManager']['abi']
# print(f"ABI: {abi}")
w3.eth.default_account = w3.eth.accounts[0]
Greeter = w3.eth.contract(abi=abi, bytecode=bytecode)


def upload_to_ipfs(file_path):
    res = client.add(file_path)
    return res['Hash']


# 生成文本哈希值
def generate_text_hash(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


# 示例：上传图片、视频和文本
image_path = '../test_res/nuoyan.jpg'
video_path = '../test_res/fountain.mp4'
text_content = 'Hello, world! This is a test text'

image_cid = upload_to_ipfs(image_path)
video_cid = upload_to_ipfs(video_path)
text_hash = generate_text_hash(text_content)

# Submit the transaction that deploys the contract
tx_hash = Greeter.constructor().transact()

# Wait for the transaction to be mined, and get the transaction receipt
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

greeter = w3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi
)

# print(greeter.functions.greet().call())
#
# tx_hash = greeter.functions.setGreeting('Nihao').transact()
# tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
# print('tx_receipt["status"])', tx_receipt['status'])
# print(greeter.functions.greet().call())
tx_hash = greeter.functions.storeData(text_hash,
                                      image_cid,
                                      video_cid).transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print('tx_receipt["status"])', tx_receipt['status'])
# print(greeter.functions.getData(1).call())
print(greeter.functions.getData(0).call())
