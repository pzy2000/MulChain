import hashlib
import ipfshttpclient
from web3 import Web3

# 连接到以太坊节点
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
assert w3.is_connected(), "Ethereum node connection failed"

# 连接到IPFS节点
client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')
assert client, "IPFS node connection failed"
# Address: 0xd632649020563a3a0554fe28faf04c6763f34ffc
# Private Key: 0x62ea27f1c68e33dd7f42f4a1abee34bdcce63531e7d121f3de3ef90625a18622
# 以太坊账户和私钥
private_key = "0x271dc1923273ca3617ed7862176db4c602a17ad4f7f63723b4639b167faad091"
address = "0xd632649020563a3a0554fe28faf04c6763f34ffc"

account = w3.eth.account.from_key(private_key)
print(f"account: {account.address}")
w3.eth.default_account = account.address
print(f"Default account: {w3.eth.default_account}")
# 查询地址余额（单位为wei）

balance_wei = w3.eth.get_balance(w3.to_checksum_address(address))

# 将余额转换为以太（Ether）
balance_ether = w3.from_wei(balance_wei, 'ether')

print(f"Address: {address}")
print(f"Balance: {balance_ether} Ether")
# 智能合约地址和ABI
manager_contract_address = '0x15de4b9fc83be608eb9bcb441351267514ec2bec'
manager_abi = []

# 实例化智能合约
manager_contract_address = w3.to_checksum_address(manager_contract_address)
manager_contract = w3.eth.contract(address=manager_contract_address, abi=manager_abi)


# 上传文件到IPFS并获取CID
def upload_to_ipfs(file_path):
    res = client.add(file_path)
    return res['Hash']


# 生成文本哈希值
def generate_text_hash(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


# 示例：上传图片、视频和文本
image_path = 'test_res/nuoyan.jpg'
video_path = 'test_res/fountain.mp4'
text_content = 'Hello, world! This is a test text'

image_cid = upload_to_ipfs(image_path)
video_cid = upload_to_ipfs(video_path)
text_hash = generate_text_hash(text_content)

print(f"Image CID: {image_cid}")
print(f"Video CID: {video_cid}")
print(f"Text Hash: {text_hash}")

# 获取最新的Nonce值
nonce = w3.eth.get_transaction_count(w3.to_checksum_address(address))

# 调用管理合约存储数据
store_data_txn = manager_contract.functions.storeData(text_hash, image_cid, video_cid).build_transaction({
    'from': w3.eth.default_account,
    'gas': 200000,
    'gasPrice': w3.to_wei('20', 'gwei'),
    'nonce': nonce,
})

signed_store_data_txn = w3.eth.account.sign_transaction(store_data_txn, private_key=private_key)
tx_hash = w3.eth.send_raw_transaction(signed_store_data_txn.rawTransaction)

# 等待交易确认
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Data stored with transaction hash: {tx_receipt.transactionHash.hex()}")

# 查询数据
entry_id = 0  # 示例数据ID
data = manager_contract.functions.getData(entry_id).call()
print(f"Stored data: {data}")
