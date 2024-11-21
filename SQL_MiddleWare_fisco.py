import os
import pickle
import random
import re
import sys
sys.path.append("../")
sys.path.append("")
sys.path.append("sdk/")
sys.path.append(os.getcwd())
import ipfshttpclient
import time
from datetime import datetime, timedelta
import sqlparse
from sqlparse.tokens import DML
from sqlparse.tokens import Token
from sdk.client.stattool import StatTool
from sdk.client.bcosclient import BcosClient
from sdk.client.datatype_parser import DatatypeParser
from sdk.client_config import client_config
from sdk.client.contractnote import ContractNote

# 从文件加载abi定义
demo_config = client_config
abi_file = "H:/PhD/Projects/web3_NFT/contracts/management_storage.abi"
data_parser = DatatypeParser()
data_parser.load_abi_file(abi_file)
bin_file = ""
contract_abi = data_parser.contract_abi

try:
    stat = StatTool.begin()
    client = BcosClient()
    print(client.getinfo())
    # 部署合约
    print("\n>>Deploy:----------------------------------------------------------")
    with open("H:/PhD/Projects/web3_NFT/contracts/management_storage.bin", 'r') as load_f:
        contract_bin = load_f.read()
        load_f.close()
    result = client.deploy(contract_bin)
    print("deploy", result)
    print("new address : ", result["contractAddress"])
    contract_name = os.path.splitext(os.path.basename(abi_file))[0]
    memo = "tx:" + result["transactionHash"]
    # 把部署结果存入文件备查
    ContractNote.save_address_to_contract_note("demo", contract_name,
                                               result["contractAddress"])
    # 发送交易，调用一个改写数据的接口
    print("\n>>sendRawTransaction:----------------------------------------------------")
    to_address = result['contractAddress']  # use new deploy address
    args = ['simplename', ]
except Exception as e:
    print(e)
from pybloom_live import BloomFilter  # 导入 Bloom 过滤器

block_sizes = [16, 32, 64, 128, 256, 512, 1024]


def generate_random_times(min_time, max_time):
    # 生成两个随机的时间差
    min_time = datetime.strptime(min_time, '%Y-%m-%d %H:%M:%S')
    max_time = datetime.strptime(max_time, '%Y-%m-%d %H:%M:%S')
    delta_a = random.randint(0, int((max_time - min_time).total_seconds()))
    delta_b = random.randint(delta_a, int((max_time - min_time).total_seconds()))

    # 计算 a 和 b 的具体时间
    a = min_time + timedelta(seconds=delta_a)
    b = min_time + timedelta(seconds=delta_b)

    return a, a


# 生成 min_time 到 max_time 之间的随机时间
def generate_random_date(min_time, max_time):
    delta = max_time - min_time
    random_seconds = random.randint(0, int(delta.total_seconds()))
    random_date = min_time + timedelta(seconds=random_seconds)
    return random_date.strftime('%Y-%m-%d')


class SQLMiddleware:
    def __init__(self, contract_instance, ipfs_client):
        # self.contract = contract_instance
        self.ipfs = ipfs_client
        # 创建布隆过滤器来跟踪已存储的哈希，避免重复存储
        self.bloom_filter = BloomFilter(capacity=45000, error_rate=0.001)
        # 存储提前缓存的数据
        self.cached_data = {}
        self.ipfs_cache = {}
        self.cached_path = {}

        # 初始化用于统计索引构建和区块生成的开销数据
        self.index_building_times = []
        self.MulChain_o_index_building_times = []
        self.block_generation_times = []
        self.index_storage_costs = []
        self.select_latency = []
        self.select_MulChain_o_latency = []
        # self.select_adder_latency = []
        # self.select_BHash_latency = []
        self.select_Trie_latency = []

        self.vo_btree_size_kb = []
        self.vo_adder_size_kb = []
        self.vo_bhashtree_size_kb = []
        self.vo_trie_size_kb = []

    def parse_query(self, query):
        # 使用 sqlparse 解析 SQL 查询
        parsed = sqlparse.parse(query)[0]
        # print("parsed", parsed)
        stmt_type = self.get_statement_type(parsed)

        if stmt_type == 'INSERT':
            return self.handle_insert(parsed)
        elif stmt_type == 'SELECT':
            return self.handle_select(parsed)
        elif stmt_type == 'UPDATE':
            return self.handle_update(parsed)
        else:
            raise ValueError("Unsupported SQL operation, query is", query)

    def get_statement_type(self, parsed):
        # 判断查询类型
        for token in parsed.tokens:
            if token.ttype is DML:
                return token.value.upper()

    def handle_insert(self, parsed):
        # 解析 INSERT 查询并进行数据存储
        table_name, values = self.extract_insert_values(parsed)

        if table_name.lower() == 'multimodal_data':
            text_hash, image_path, video_path, timestamp = values
            index_start_time = time.time()

            # 将图片和视频上传到 IPFS
            try:
                # if image_path not in self.ipfs_cache or video_path not in self.ipfs_cache:
                image_cid = self.ipfs.add(image_path)['Hash']
                video_cid = self.ipfs.add(video_path)['Hash']

                self.ipfs_cache[image_path] = image_cid
                self.ipfs_cache[video_path] = video_cid
                # else:
                #     image_cid = self.ipfs_cache.get(image_path)
                #     video_cid = self.ipfs_cache.get(video_path)
            except Exception as e:
                print("IPFS Error", e)
                image_cid = "0"
                video_cid = "0"
            index_off_start_time = time.time()

            # 调用区块链合约的 storeData 方法并记录区块生成时间
            block_start_time = time.time()
            # print("timestamp:", timestamp)
            # tx_hash = self.contract.functions.storeData(text_hash, image_cid, video_cid, timestamp).transact()
            receipt = client.sendRawTransactionGetReceipt(to_address, contract_abi, "storeData", [text_hash, image_cid, video_cid, timestamp])
            if receipt['status'] == "0x0":
                pass
            else:
                print("Error, receipt['status']", receipt['status'])
            # print("receipt:", receipt)
            # 手动生成新区块
            block_end_time = time.time()

            # 记录索引构建和区块生成开销
            index_end_time = time.time()
            self.index_building_times.append(index_end_time - index_start_time)
            self.MulChain_o_index_building_times.append(index_end_time - index_off_start_time)
            self.block_generation_times.append(block_end_time - block_start_time)

            # 计算索引存储成本
            cached_data_size = sys.getsizeof(pickle.dumps(self.cached_data))
            bloom_filter_size = sys.getsizeof(pickle.dumps(self.bloom_filter))
            total_size_kb = (cached_data_size + bloom_filter_size) / 1024 / 1024
            self.index_storage_costs.append(total_size_kb)  # 以 KB 为单位

            return f"Data inserted with transaction hash: {666}"

    def extract_time_range(self, condition):
        # 提取 BETWEEN 子句中的时间范围
        match = re.search(r'BETWEEN\s*\'([^\']*)\'\s*AND\s*\'([^\']*)\'', condition, re.IGNORECASE)
        if match:
            return match.group(1), match.group(2)
        else:
            raise ValueError("Invalid BETWEEN clause in SELECT statement.")

    def handle_select(self, parsed):
        select_start_time = time.time()
        # 解析 SELECT 查询并进行数据查询
        table_name, condition = self.extract_select_conditions(parsed)

        if table_name.lower() == 'multimodal_data':
            # 检查是否是时间范围查询
            if 'BETWEEN' in condition.upper():
                start_time, end_time = self.extract_time_range(condition)
                results = []
                if results:
                    on_chain_select_end_time = time.time()
                    self.select_MulChain_o_latency.append(on_chain_select_end_time - select_start_time)
                    select_end_time = time.time()
                    self.select_latency.append(select_end_time - select_start_time)
                    return results
                else:
                    # 如果缓存中没有符合条件的数据，则从区块链中查询
                    results = []
                    results1 = []


                    # data_btree = self.contract.functions.getDataByTimeRange(start_time, end_time).call()
                    # print("getDataByTimeRange to_address,", to_address)
                    data_btree = client.call(to_address, contract_abi, "getDataByTimeRange", [start_time, end_time])
                    wasted_time_on = 0
                    if data_btree[3]:
                        print("results", results)
                        results.append({
                            "text_hash": data_btree[0],
                            "image_cid": data_btree[1],
                            "video_cid": data_btree[2],
                            "timestamp": data_btree[3]
                        })
                    wasted_time_on_s = time.time()
                    try:
                        image_path = "sample_image.jpg"  # 请替换为实际图片路径
                        video_path = "sample_video.mp4"  # 请替换为实际视频路径
                        _ = self.ipfs.get(self.ipfs_cache[image_path], target=f"./cache/{self.ipfs_cache[image_path]}")
                        _ = self.ipfs.get(self.ipfs_cache[video_path], target=f"./cache/{self.ipfs_cache[video_path]}")
                    except Exception as e:
                        print(e)
                    wasted_time_on_e = time.time()
                    wasted_time_on += wasted_time_on_e - wasted_time_on_s
                    select_end_time = time.time()
                    self.select_latency.append(select_end_time - select_start_time)
                    self.select_MulChain_o_latency.append(select_end_time - select_start_time - wasted_time_on)
                    return results
            # 检查是否是前缀匹配查询
            elif 'LIKE' in condition.upper():
                prefix = self.extract_prefix_condition(condition)
                results = []
                wasted_time = 0
                # for entry_id in range(self.contract.functions.entryCount().call()):
                for entry_id in range(client.call(to_address, contract_abi, "entryCount").call()):
                    # data = self.contract.functions.getData(entry_id).call()
                    data = client.call(to_address, contract_abi, "getData", [entry_id]).call()
                    wasted_time_start = time.time()
                    wasted_time_end = time.time()
                    wasted_time += wasted_time_end - wasted_time_start
                    if data[3].startswith(prefix):
                        results.append({
                            "text_hash": data[0],
                            "image_cid": data[1],
                            "video_cid": data[2],
                            "timestamp": data[3]
                        })

                select_end_time = time.time()

                select_start_time_trie = time.time()
                # data_trie = self.contract.functions.getDataByFuzzy(prefix).call()
                data_trie = client.call(to_address, contract_abi, "getDataByFuzzy", [prefix]).call()
                on_chain_select_end_time = time.time()
                self.select_MulChain_o_latency.append(on_chain_select_end_time - select_start_time_trie)
                on_chain_time_s = time.time()
                if results:
                    try:
                        image_path = self.ipfs.get(results[0]['image_cid'], target=f"./cache/{results[0]['image_cid']}")
                        video_path = self.ipfs.get(results[0]['video_cid'], target=f"./cache/{results[0]['video_cid']}")
                    except Exception as e:
                        print(e)

                on_chain_time_e = time.time()
                on_chain_time_used = on_chain_time_e - on_chain_time_s
                select_end_time_trie = time.time()
                self.select_Trie_latency.append(select_end_time_trie - select_start_time_trie)
                self.select_adder_latency.append(select_end_time - select_start_time - wasted_time + on_chain_time_used)
                results_trie = data_trie
                if results != results_trie and (len(results) != len(results_trie[0])):
                    print("results mismatch")
                    print("results: ", len(results))
                    print("results_trie: ", len(results_trie[0]))
                return results
            else:
                # 单条记录查询
                entry_id = int(condition.split('=')[1].strip())
                # 使用布隆过滤器加速查询
                if str(entry_id) in self.bloom_filter:
                    print("enter bloom")
                    # 如果在布隆过滤器中，返回缓存的数据
                    cached_data = self.cached_data.get(str(entry_id), None)
                    # print("cache_data", cached_data)
                    if cached_data:
                        on_chain_select_end_time = time.time()
                        self.select_MulChain_o_latency.append(on_chain_select_end_time - select_start_time)
                        select_end_time = time.time()
                        self.select_latency.append(select_end_time - select_start_time)
                        return cached_data
                    else:
                        on_chain_select_end_time = time.time()
                        self.select_MulChain_o_latency.append(on_chain_select_end_time - select_start_time)
                        select_end_time = time.time()
                        self.select_latency.append(select_end_time - select_start_time)
                        return "Data not found in cached storage."
                else:
                    # 如果不在布隆过滤器中，去区块链查询
                    # data = self.contract.functions.getData(entry_id).call()
                    data = client.call(to_address, contract_abi, "getData", [entry_id]).call()
                    # 将查询到的数据添加到布隆过滤器和缓存中
                    self.bloom_filter.add(str(entry_id))
                    self.cached_data[str(entry_id)] = {
                        "text_hash": data[0],
                        "image_cid": data[1],
                        "video_cid": data[2],
                        "timestamp": data[3]
                    }
                    on_chain_select_end_time = time.time()
                    self.select_MulChain_o_latency.append(on_chain_select_end_time - select_start_time)
                    try:
                        image_path = self.ipfs.get(data[1], target=f"./cache/{data[1]}")
                        video_path = self.ipfs.get(data[2], target=f"./cache/{data[2]}")
                    except Exception as e:
                        print(e)
                    select_end_time = time.time()
                    self.select_latency.append(select_end_time - select_start_time)
                    # gas_a = self.contract.functions.getData(entry_id).estimate_gas(
                    #     {'from': w3.eth.default_account})
                    # self.vo_adder_size_kb.append(gas_a / gas_per_kb)
                    return self.cached_data[str(entry_id)]

    def extract_prefix_condition(self, condition):
        # 提取 LIKE 查询中的前缀条件
        match = re.search(r"LIKE\s+'(.*?)%'", condition, re.IGNORECASE)
        if match:
            return match.group(1)
        else:
            raise ValueError("Invalid LIKE condition in SELECT statement.")

    def handle_update(self, parsed):
        # 解析 UPDATE 查询并进行数据更新
        table_name, update_values, condition = self.extract_update_values(parsed)

        if table_name.lower() == 'multimodal_data':
            # 从条件中提取 entry_id，确保条件的格式是 entry_id = value
            if "entry_id" in condition:
                entry_id = int(condition.split('=')[1].strip())
            else:
                raise ValueError("Invalid condition in UPDATE statement. Expected 'entry_id = value'.")

            new_text_hash, new_image_path, new_video_path = update_values

            # 更新图片和视频到 IPFS
            new_image_cid = self.ipfs.add(new_image_path)['Hash']
            new_video_cid = self.ipfs.add(new_video_path)['Hash']
            timestamp = None

            # 调用区块链合约的 updateData 方法
            tx_hash = self.contract.functions.updateData(entry_id, new_text_hash, new_image_cid,
                                                         new_video_cid, timestamp).transact()
            # 手动生成新区块
            # w3.provider.make_request("evm_mine", [])
            # tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

            # 更新缓存的数据
            if str(entry_id) in self.cached_data:
                self.cached_data[str(entry_id)] = {
                    "text_hash": new_text_hash,
                    "image_cid": new_image_cid,
                    "video_cid": new_video_cid,
                    "timestamp": timestamp
                }

            return f"Data updated with transaction hash: {666}"

    def extract_insert_values(self, parsed):
        tokens = [token for token in parsed.tokens if not token.is_whitespace]
        # print("Tokens:", [token.value for token in tokens])  # 打印 token 内容
        table_name = None
        values = []

        # 遍历 Tokens，提取表名和插入值
        for i, token in enumerate(tokens):
            # 找到表名
            if token.ttype is Token.Keyword and token.value.upper() == "INTO":
                # 提取表名部分
                table_with_columns = tokens[i + 1].value
                table_name = table_with_columns.split()[0]

            # 找到 VALUES 并提取后面的值
            if token.value.upper().startswith("VALUES"):
                # 使用正则表达式从 VALUES 子句提取值
                values_str = re.search(r'VALUES\s*\((.*)\)', token.value, re.IGNORECASE)
                if values_str:
                    values = [val.strip().strip("'") for val in values_str.group(1).split(",")]
                    break

        if not table_name:
            raise ValueError("Table name not found in INSERT statement.")

        if len(values) == 0:
            raise ValueError("No values found in INSERT statement.")

        return table_name, values

    def extract_select_conditions(self, parsed):
        # 提取 SELECT 语句中的表名和条件
        tokens = [token for token in parsed.tokens if not token.is_whitespace]
        table_name = tokens[3].get_real_name()  # 获取表名
        condition = tokens[-1].value  # 获取条件
        return table_name, condition

    def extract_update_values(self, parsed):
        tokens = [token for token in parsed.tokens if not token.is_whitespace]

        table_name = None
        set_values = []
        condition = None

        for i, token in enumerate(tokens):

            # 找到表名
            if token.ttype is Token.Keyword.DML and token.value.upper() == "UPDATE":
                # 提取表名部分
                if i + 1 < len(tokens):
                    table_name = tokens[i + 1].get_real_name()
                    # print("Table Name:", table_name)

            # 找到 SET 并提取后面的值
            if token.ttype is Token.Keyword and token.value.upper() == "SET":
                if i + 1 < len(tokens):
                    set_token = tokens[i + 1]
                    # 将 SET 子句的内容拆分为键值对列表
                    set_values = [val.strip() for val in set_token.value.split(",")]

            # 找到 WHERE 子句
            if token.value.upper().startswith("WHERE"):
                # 直接获取 WHERE 子句中的条件部分
                condition = token.value[len("WHERE"):].strip()

                break

        # 提取具体的更新值
        update_values = []
        for value_pair in set_values:
            key_value = value_pair.split("=")
            if len(key_value) == 2:
                key, value = key_value
                update_values.append(value.strip().strip("'"))

        if not table_name:
            raise ValueError("Table name not found in UPDATE statement.")

        if len(update_values) != 3:
            raise ValueError("Incorrect number of values found in UPDATE statement.")

        if not condition:
            raise ValueError("Condition not found in UPDATE statement.")

        return table_name, update_values, condition


if __name__ == '__main__':
    with open('data_list.pkl', 'rb') as f:
        data_list = pickle.load(f)

    time_stamp_list = []
    for data in data_list:
        # 解析日期字符串为 datetime 对象
        dt_object = datetime.strptime(data['time_stamp'], '%Y-%m-%d %H:%M:%S')
        # 将 datetime 对象转换为日期字符串
        formatted_date = dt_object.strftime('%Y-%m-%d %H:%M:%S')
        # data['time_stamp'] = formatted_date
        time_stamp_list.append(formatted_date)

    min_time = min(time_stamp_list)
    max_time = max(time_stamp_list)
    print("min_time:", min_time)
    print("max_time:", max_time)
    # 生成随机日期
    ipfs_client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')  # 替换为你的 IPFS 节点地址
    abi_file = "H:/PhD/Projects/web3_NFT/contracts/management_storage.abi"
    data_parser = DatatypeParser()
    data_parser.load_abi_file(abi_file)
    contract_abi = data_parser.contract_abi
    # 部署合约
    sql_client = SQLMiddleware(contract_abi, ipfs_client)
    text_hash = "6666"
    time_stamp = "666666"
    image_path = r"H:\PhD\Projects\web3_NFT\sample_image.jpg"  # 请替换为实际图片路径
    video_path = r"H:\PhD\Projects\web3_NFT\sample_video.mp4"  # 请替换为实际视频路径
    insert_query = f"INSERT INTO multimodal_data (textHash, imageCID, videoCID, timestamp) VALUES ('{text_hash}', '{image_path}', '{video_path}', '{time_stamp}')"
    sql_client.parse_query(insert_query)
    a, b = generate_random_times(min_time, max_time)
    select_query = f"SELECT * FROM multimodal_data WHERE timestamp BETWEEN '{a}' AND '{b}'"
    sql_client.parse_query(select_query)
    print("exit")
    client.finish()
    sys.exit(0)