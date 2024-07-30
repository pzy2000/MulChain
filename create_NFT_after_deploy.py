from web3 import Web3

# Connect to the local Ethereum node
local_url = 'http://127.0.0.1:8545'
w3 = Web3(Web3.HTTPProvider(local_url))

# Check if connected
print(f"Connected: {w3.is_connected()}")
import json

# Load the contract ABI
with open('compiled_code.json', 'r') as file:
    compiled_sol = json.load(file)

abi = compiled_sol['contracts']['SimpleNFT.sol']['SimpleNFT']['abi']

# The address of the deployed contract
contract_address = '0x97c518F54b48caEc67017a61f96E7E23e5173a7C'
