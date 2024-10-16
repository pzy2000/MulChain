// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./MultiModalStorage.sol";


contract MultiModalQuery {
    MultiModalStorage storageContract;

    constructor(address _storageContractAddress) {
        storageContract = MultiModalStorage(_storageContractAddress);
    }

    function queryData(uint256 _entryId) public view returns (string memory, string memory, string memory, uint256) {
        return storageContract.getData(_entryId);
    }
}
