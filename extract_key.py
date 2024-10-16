from web3 import Web3
# 连接到以太坊节点
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
assert w3.is_connected(), "Ethereum node connection failed"
with open(r'D:\Geth\db\keystore\UTC--2024-08-09T06-31-43.787879100Z--d632649020563a3a0554fe28faf04c6763f34ffc') as keyfile:
    encrypted_key = keyfile.read()
    private_key = w3.eth.account.decrypt(encrypted_key, '123456')
    print(f"Private key: {private_key.hex()}")