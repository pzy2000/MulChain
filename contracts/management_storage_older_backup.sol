// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MultiModalStorageManager {
    string public greeting;
    // 定义一个结构体来存储每个数据条目的信息
    struct DataEntry {
        string textHash;
        string imageCID;
        string videoCID;
        uint256 timestamp;
    }

    // 使用映射来存储所有数据条目
    mapping(uint256 => DataEntry) public dataEntries;
    uint256 public entryCount;

    // 定义一个事件，在数据存储时触发
    event DataStored(uint256 indexed entryId, string textHash, string imageCID, string videoCID, uint256 timestamp);
    constructor() public {
            greeting = 'Hello';
        }
    // 存储数据的方法
    function storeData(string memory _textHash, string memory _imageCID, string memory _videoCID) public returns(uint256){
        dataEntries[entryCount] = DataEntry({
            textHash: _textHash,
            imageCID: _imageCID,
            videoCID: _videoCID,
            timestamp: block.timestamp
        });
        emit DataStored(entryCount, _textHash, _imageCID, _videoCID, block.timestamp);
        entryCount++;
        return entryCount-1;
    }
    function setGreeting(string memory _greeting) public {
            greeting = _greeting;
        }
    function greet() view public returns (string memory) {
            return greeting;
        }

    // 查询数据的方法
    function getData(uint256 _entryId) public view returns (string memory, string memory, string memory, uint256) {
        DataEntry memory entry = dataEntries[_entryId];
        return (entry.textHash, entry.imageCID, entry.videoCID, entry.timestamp);
    }

    // 更新数据的方法
    function updateData(uint256 _entryId, string memory _newTextHash, string memory _newImageCID, string memory _newVideoCID) public {
        require(_entryId < entryCount, "Entry ID does not exist");
        DataEntry storage entry = dataEntries[_entryId];
        entry.textHash = _newTextHash;
        entry.imageCID = _newImageCID;
        entry.videoCID = _newVideoCID;
        entry.timestamp = block.timestamp;
        emit DataStored(_entryId, _newTextHash, _newImageCID, _newVideoCID, block.timestamp);
    }
}
