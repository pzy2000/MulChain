import json
from solcx import compile_standard, install_solc, set_solc_version
from web3 import Web3

# 安装和设置Solidity编译器版本
install_solc("0.8.20")
set_solc_version("0.8.20")

with open("SimpleNFT.sol", "r") as file:
    simple_nft_file = file.read()

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleNFT.sol": {"content": simple_nft_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
                }
            }
        },
    },
    allow_paths=[".", "./@openzeppelin/contracts"]
)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# 连接到本地以太坊节点
local_url = 'http://127.0.0.1:8545'
w3 = Web3(Web3.HTTPProvider(local_url))

# 使用提供的以太坊账户
private_key = "0xbd14b43d5dca801a85f6cb8898c641ed4e6ceb86cb29a1e3398392d4ebbf0d30"
address = "0x6dca30839253075f48753ef37bc2315e2b8c28d1"

print(f"Ethereum Address: {address}")
print(f"Private Key: {private_key}")

# 选择账户
account = w3.eth.account.from_key(private_key)
w3.eth.default_account = account.address
print(f"Default Account: {w3.eth.default_account}")

# 获取最新区块的Gas限制
latest_block = w3.eth.get_block('latest')
block_gas_limit = latest_block['gasLimit']
print(f"Block Gas Limit: {block_gas_limit}")

# 确保设置的Gas限制小于区块Gas限制
gas_limit = 3000000

# 部署智能合约
bytecode = compiled_sol['contracts']['SimpleNFT.sol']['SimpleCollectible']['evm']['bytecode']['object']
# print(f"Bytecode: {bytecode}")
abi = compiled_sol['contracts']['SimpleNFT.sol']['SimpleCollectible']['abi']
# print(f"ABI: {abi}")
# exit(666)
gas_price = w3.eth.gas_price  # 或者指定一个合理的gas price
SimpleNFT = w3.eth.contract(abi=abi, bytecode=bytecode)
address = w3.to_checksum_address('0x6dca30839253075f48753ef37bc2315e2b8c28d1')
nonce = w3.eth.get_transaction_count(address)
# 构建交易
initial_owner_address = w3.eth.default_account
print(f"Initial Owner Address: {initial_owner_address}")
transaction = SimpleNFT.constructor().build_transaction({
    'value': w3.to_wei(0.2, 'ether'),  # 发送0.1 ETH
    'gas': gas_limit,
    'gasPrice': gas_price,
    'nonce': nonce,
})
# tx_hash = SimpleNFT.constructor(initial_owner_address).transact()
# 查询余额
balance = w3.eth.get_balance(address)

# 将余额从Wei转换为Ether并输出
balance_in_ether = w3.from_wei(balance, 'ether')
print(f'Balance: {balance_in_ether} ETH (Wei: {balance})')

# 签署交易
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)

# 发送交易
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# 等待交易确认
# try:
#     tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash, timeout=600)
#     print(f'Contract deployed at address: {tx_receipt.contractAddress}')
# except exceptions.TimeExhausted:
#     print('Transaction was not confirmed in time, please try again with a higher gas price.')
#     exit(666)
print('tx_receipt["status"])', tx_receipt['status'])
print('eth.get_code()', w3.eth.get_code(tx_receipt.contractAddress))

greeter = w3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi
)

# contract_address = tx_receipt.contractAddress
# simple_nft = w3.eth.contract(address=contract_address, abi=abi)
# nonce = w3.eth.get_transaction_count(address)
# # 调用createNFT方法
# create_txn = simple_nft.functions.createNFT().build_transaction({
#     'gas': gas_limit,
#     'gasPrice': gas_price,
#     'nonce': nonce,
# })
#
# signed_create_txn = w3.eth.account.sign_transaction(create_txn, private_key=private_key)
# tx_create_hash = w3.eth.send_raw_transaction(signed_create_txn.rawTransaction)
#
# # 等待交易确认
# tx_create_receipt = w3.eth.wait_for_transaction_receipt(tx_create_hash, timeout=600)
# print(f'NFT created with transaction hash: {tx_create_receipt.transactionHash.hex()}')
# print(greeter.functions.multiply(1).call())
