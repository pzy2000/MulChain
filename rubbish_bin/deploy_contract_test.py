from web3 import Web3
from solcx import compile_source, install_solc, set_solc_version
install_solc("0.8.20")
set_solc_version("0.8.20")
print(1111)
# Solidity source code
compiled_sol = compile_source(
    '''
    pragma solidity >0.5.0;

    contract Greeter {
        string public greeting;

        constructor() public {
            greeting = 'Hello';
        }

        function setGreeting(string memory _greeting) public {
            greeting = _greeting;
        }

        function greet() view public returns (string memory) {
            return greeting;
        }
    }
    ''',
    output_values=['abi', 'bin']
)
print(2222)

# retrieve the contract interface
contract_id, contract_interface = compiled_sol.popitem()

# get bytecode / bin
bytecode = contract_interface['bin']

# get abi
abi = contract_interface['abi']

# web3.py instance
w3 = Web3(Web3.EthereumTesterProvider())

# set pre-funded account as sender
w3.eth.default_account = w3.eth.accounts[0]

Greeter = w3.eth.contract(abi=abi, bytecode=bytecode)
print(3333)

# Submit the transaction that deploys the contract
tx_hash = Greeter.constructor().transact()

# Wait for the transaction to be mined, and get the transaction receipt
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

greeter = w3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi
)
print(4444)

print(greeter.functions.greet().call())
print(5555)

tx_hash = greeter.functions.setGreeting('Nihao').transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(greeter.functions.greet().call())