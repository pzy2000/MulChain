// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MultiModalStorageManager {
    string public greeting;

    // 定义一个结构体来存储每个数据条目的信息
    struct DataEntry {
        string textHash;    // 文本的哈希值，用于唯一标识文本内容
        string imageCID;    // 图像的CID (Content Identifier)，用于存储在IPFS等去中心化存储中
        string videoCID;    // 视频的CID (Content Identifier)
        string timestamp;   // 存储数据条目的时间戳
    }

    // 使用映射来存储所有数据条目，键为数据条目的ID，值为DataEntry结构体
    mapping(uint256 => DataEntry) public dataEntries;
    uint256 public entryCount;  // 存储数据条目的计数器

    // B+树节点结构体定义
    struct BPlusTreeNode {
        bool isLeaf; // 是否是叶子节点
        uint256[] keys; // 存储时间戳对应的键
        uint256[] children; // 存储子节点的ID（如果是叶子节点则为空）
        uint256[] dataEntryIds; // 存储数据条目ID（仅叶子节点有效）
    }

    // B+树存储
    mapping(uint256 => BPlusTreeNode) public bPlusTreeNodes;
    uint256 public rootId;  // 根节点ID
    uint256 public nodeCount; // 节点计数器

    // 定义一个事件，在数据存储时触发，方便监听存储操作
    event DataStored(uint256 indexed entryId, string textHash, string imageCID, string videoCID, string timestamp);
    event NodeCreated(uint256 nodeId, bool isLeaf, uint256[] keys);

    // 构造函数，初始化合约的greeting变量和根节点
    constructor() public {
        greeting = 'Hello';
        // 初始化根节点为叶子节点
        rootId = nodeCount;
        bPlusTreeNodes[rootId] = BPlusTreeNode({
            isLeaf: true,
            keys: new uint256[](0),
            children: new uint256[](0),
            dataEntryIds: new uint256[](0)
        });
        nodeCount++;
        emit NodeCreated(rootId, true, new uint256[](0));
    }

    // 存储数据的方法，返回存储数据的条目ID
    function storeData(string memory _textHash, string memory _imageCID, string memory _videoCID, string memory _timestamp) public returns (uint256) {
        // 创建一个新的数据条目并存储在映射中
        dataEntries[entryCount] = DataEntry({
            textHash: _textHash,
            imageCID: _imageCID,
            videoCID: _videoCID,
            timestamp: _timestamp
        });

        // 触发数据存储事件，方便监听
        emit DataStored(entryCount, _textHash, _imageCID, _videoCID, _timestamp);

        // 将数据条目插入到B+树中
        insertToBPlusTree(entryCount, _timestamp);

        // 增加数据条目计数器
        entryCount++;
        return entryCount - 1;  // 返回新存储的条目ID
    }

    // 设置greeting变量的值
    function setGreeting(string memory _greeting) public {
        greeting = _greeting;
    }

    // 返回greeting变量的值
    function greet() view public returns (string memory) {
        return greeting;
    }

    // 查询数据的方法，传入条目ID，返回对应的数据条目
    function getData(uint256 _entryId) public view returns (string memory, string memory, string memory, string memory) {
        DataEntry memory entry = dataEntries[_entryId];
        return (entry.textHash, entry.imageCID, entry.videoCID, entry.timestamp);
    }

    // 更新数据的方法，传入条目ID和新的数据，更新对应条目
    function updateData(uint256 _entryId, string memory _newTextHash, string memory _newImageCID, string memory _newVideoCID, string memory _newtimestamp) public {
        require(_entryId < entryCount, "Entry ID does not exist");  // 确保条目ID存在
        DataEntry storage entry = dataEntries[_entryId];  // 获取对应的条目
        entry.textHash = _newTextHash;  // 更新文本哈希值
        entry.imageCID = _newImageCID;  // 更新图像CID
        entry.videoCID = _newVideoCID;  // 更新视频CID
        entry.timestamp = _newtimestamp;  // 更新时间戳

        // 触发数据存储事件，表示条目已更新
        emit DataStored(_entryId, _newTextHash, _newImageCID, _newVideoCID, _newtimestamp);
    }

    // 插入到B+树中的方法
    function insertToBPlusTree(uint256 entryId, string memory timestamp) internal {
        // 将字符串时间戳转换为uint256表示
        uint256 timeKey = stringToUint(timestamp);

        // 插入到根节点（简单实现，未包含节点分裂逻辑）
        BPlusTreeNode storage rootNode = bPlusTreeNodes[rootId];

        // 如果是叶子节点，直接插入
        if (rootNode.isLeaf) {
            rootNode.keys.push(timeKey);
            rootNode.dataEntryIds.push(entryId);
        } else {
            // TODO: 实现非叶子节点的插入逻辑
        }
    }

    // 时间范围查询的方法，返回在指定时间范围内的数据条目
    function getDataByTimeRange(string memory _startTime, string memory _endTime) public view returns (string[] memory, string[] memory, string[] memory, string[] memory) {
        uint256 startKey = stringToUint(_startTime);
        uint256 endKey = stringToUint(_endTime);

        // 临时存储符合条件的条目ID
        uint256[] memory resultEntryIds = new uint256[](entryCount);
        uint256 count = 0;

        // 遍历B+树的根节点，找到符合时间范围的条目ID
        BPlusTreeNode storage rootNode = bPlusTreeNodes[rootId];
        if (rootNode.isLeaf) {
            for (uint256 i = 0; i < rootNode.keys.length; i++) {
                if (rootNode.keys[i] >= startKey && rootNode.keys[i] <= endKey) {
                    resultEntryIds[count] = rootNode.dataEntryIds[i];
                    count++;
                }
            }
        } else {
            // TODO: 实现非叶子节点的查询逻辑
        }

        // 创建一个大小合适的数组来存储符合条件的条目
        string[] memory textHashes = new string[](count);
        string[] memory imageCIDs = new string[](count);
        string[] memory videoCIDs = new string[](count);
        string[] memory timestamps = new string[](count);
        for (uint256 j = 0; j < count; j++) {
            DataEntry memory entry = dataEntries[resultEntryIds[j]];
            textHashes[j] = entry.textHash;
            imageCIDs[j] = entry.imageCID;
            videoCIDs[j] = entry.videoCID;
            timestamps[j] = entry.timestamp;
        }
        return (textHashes, imageCIDs, videoCIDs, timestamps);
    }

    // 辅助函数，用于比较字符串（例如比较时间戳）
    function compareStrings(string memory a, string memory b) internal pure returns (int) {
        bytes memory aBytes = bytes(a);
        bytes memory bBytes = bytes(b);
        uint minLength = aBytes.length;
        if (bBytes.length < minLength) {
            minLength = bBytes.length;
        }

        // 字符逐个比较，找到第一个不相等的字符
        for (uint i = 0; i < minLength; i++) {
            if (aBytes[i] < bBytes[i]) {
                return -1;  // a 小于 b
            } else if (aBytes[i] > bBytes[i]) {
                return 1;   // a 大于 b
            }
        }

        // 如果所有字符都相等，比较字符串长度
        if (aBytes.length < bBytes.length) {
            return -1;  // a 长度小于 b
        } else if (aBytes.length > bBytes.length) {
            return 1;   // a 长度大于 b
        } else {
            return 0;   // a 和 b 完全相等
        }
    }

    // 辅助函数，将字符串转换为uint256
    function stringToUint(string memory s) internal pure returns (uint256) {
        bytes memory b = bytes(s);
        uint256 result = 0;
        for (uint i = 0; i < b.length; i++) {
            if (b[i] >= 0x30 && b[i] <= 0x39) { // 检查是否是数字字符
                result = result * 10 + (uint8(b[i]) - 48);
            }
        }
        return result;
    }
}