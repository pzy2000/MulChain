from web3 import Web3
w3 = Web3(Web3.EthereumTesterProvider())  # 使用 EthereumTesterProvider 作为测试链
w3.eth.default_account = w3.eth.accounts[0]
