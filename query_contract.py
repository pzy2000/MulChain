import pprint

from web3 import Web3
from solcx import compile_standard, install_solc, set_solc_version
# 安装和设置Solidity编译器版本
install_solc("0.8.20")
set_solc_version("0.8.20")
# 连接到Sepolia测试网络
local_url = 'http://127.0.0.1:8545'
w3 = Web3(Web3.HTTPProvider(local_url))

# 合约ABI
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

abi = compiled_sol['contracts']['SimpleNFT.sol']['SimpleCollectible']['abi']
# pprint.pprint(abi)

# 已部署合约地址
contract_address = '0x03a9672f16b262d27c8389180b9a720ea9bfcb57'

# 实例化合约对象
contract = w3.eth.contract(address=w3.to_checksum_address(contract_address), abi=abi)

# 检查合约代码是否存在
code = w3.eth.get_code(w3.to_checksum_address(contract_address))
if code == b'':  # 如果返回空字节串，表示合约不存在
    print(f"No contract found at address {contract_address}")
else:
    print(f"Contract code at address {contract_address}")

    # 调用合约函数（例如获取合约的名称）
    # try:
    create_Collectible = contract.functions.createCollectible("H:\PhD\Projects\web3\metadata\metadata.json").call()
    # symbol = contract.functions.symbol().call()
    # total_supply = contract.functions.totalSupply().call()
    print(f"Contract createCollectible: {create_Collectible}")
    # print(f"Contract Symbol: {symbol}")
    # print(f"Total Supply: {total_supply}")
    # except Exception as e:
    #     print(f"An error occurred: {e}")
