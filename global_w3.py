from web3 import Web3
from eth_tester import PyEVMBackend, EthereumTester
genesis_overrides = {'gas_limit': 450000000000}
custom_genesis_params = PyEVMBackend.generate_genesis_params(overrides=genesis_overrides)
pyevm_backend = PyEVMBackend(genesis_parameters=custom_genesis_params)
t = EthereumTester(backend=pyevm_backend)
w3 = Web3(Web3.EthereumTesterProvider(t))  # 使用 EthereumTesterProvider 作为测试链
w3.eth.default_account = w3.eth.accounts[0]


