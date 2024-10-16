import re
import sqlparse
from sqlparse.tokens import DML
from sqlparse.tokens import Token
from global_w3 import w3
from pybloom_live import BloomFilter  # 导入 Bloom 过滤器


class SQLMiddleware:
    def __init__(self, contract_instance, ipfs_client):
        self.contract = contract_instance
        self.ipfs = ipfs_client
        # 创建布隆过滤器来跟踪已存储的哈希，避免重复存储
        self.bloom_filter = BloomFilter(capacity=1000, error_rate=0.001)
        # 存储提前缓存的数据
        self.cached_data = {}

    def parse_query(self, query):
        # 使用 sqlparse 解析 SQL 查询
        parsed = sqlparse.parse(query)[0]
        stmt_type = self.get_statement_type(parsed)

        if stmt_type == 'INSERT':
            return self.handle_insert(parsed)
        elif stmt_type == 'SELECT':
            return self.handle_select(parsed)
        elif stmt_type == 'UPDATE':
            return self.handle_update(parsed)
        else:
            raise ValueError("Unsupported SQL operation")

    def get_statement_type(self, parsed):
        # 判断查询类型
        for token in parsed.tokens:
            if token.ttype is DML:
                return token.value.upper()

    def handle_insert(self, parsed):
        # 解析 INSERT 查询并进行数据存储
        table_name, values = self.extract_insert_values(parsed)

        if table_name.lower() == 'multimodal_data':
            text_hash, image_path, video_path = values
            print("parse completed")
            # 将图片和视频上传到 IPFS
            image_cid = self.ipfs.add(image_path)['Hash']
            video_cid = self.ipfs.add(video_path)['Hash']
            print("image_cid", image_cid)
            print("video_cid", video_cid)
            print("ipfs add completed")
            # 调用区块链合约的 storeData 方法
            tx_hash = self.contract.functions.storeData(text_hash, image_cid, video_cid).transact()
            print("tx_hash:", tx_hash)
            tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
            if tx_receipt['status'] == 1:
                print("Success", "Data stored on blockchain successfully!")
                # 将新哈希加入布隆过滤器
                self.bloom_filter.add(str(tx_receipt['transactionIndex']))
                # 将数据加入缓存
                self.cached_data[str(tx_receipt['transactionIndex'])] = {
                    "text_hash": text_hash,
                    "image_cid": image_cid,
                    "video_cid": video_cid,
                    "timestamp": w3.eth.get_block('latest').timestamp
                }
            else:
                print("Error", "Transaction failed!")
            return f"Data inserted with transaction hash: {tx_receipt.transactionHash.hex()}"

    def handle_select(self, parsed):
        # 解析 SELECT 查询并进行数据查询
        table_name, condition = self.extract_select_conditions(parsed)

        if table_name.lower() == 'multimodal_data':
            entry_id = int(condition.split('=')[1].strip())
            # 使用布隆过滤器加速查询
            if str(entry_id) in self.bloom_filter:
                # 如果在布隆过滤器中，返回缓存的数据
                print("hit bloom cache, entry_id", entry_id)
                return self.cached_data.get(str(entry_id), "Data not found in cached storage.")
            else:
                # 如果不在布隆过滤器中，去区块链查询
                data = self.contract.functions.getData(entry_id).call()
                # 将查询到的数据添加到布隆过滤器和缓存中
                self.bloom_filter.add(str(entry_id))
                self.cached_data[str(entry_id)] = {
                    "text_hash": data[0],
                    "image_cid": data[1],
                    "video_cid": data[2],
                    "timestamp": data[3]
                }
                return self.cached_data[str(entry_id)]

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

            # 调用区块链合约的 updateData 方法
            tx_hash = self.contract.functions.updateData(entry_id, new_text_hash, new_image_cid,
                                                         new_video_cid).transact()
            # 手动生成新区块
            w3.provider.make_request("evm_mine", [])
            tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

            # 更新缓存的数据
            if str(entry_id) in self.cached_data:
                self.cached_data[str(entry_id)] = {
                    "text_hash": new_text_hash,
                    "image_cid": new_image_cid,
                    "video_cid": new_video_cid,
                    "timestamp": w3.eth.get_block('latest').timestamp
                }

            return f"Data updated with transaction hash: {tx_receipt.transactionHash.hex()}"

    def extract_insert_values(self, parsed):
        tokens = [token for token in parsed.tokens if not token.is_whitespace]
        # print("Tokens:", [token.value for token in tokens])  # 打印 token 内容
        table_name = None
        values = []

        # 遍历 Tokens，提取表名和插入值
        for i, token in enumerate(tokens):
            # print("token.ttype:", token.ttype)
            # print("token.value:", token.value)

            # 找到表名
            if token.ttype is Token.Keyword and token.value.upper() == "INTO":
                # 提取表名部分
                table_with_columns = tokens[i + 1].value
                table_name = table_with_columns.split()[0]
                # print("Table Name:", table_name)

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
        # print("Tokens:", [token.value for token in tokens])  # 打印 token 内容
        table_name = None
        set_values = []
        condition = None

        for i, token in enumerate(tokens):
            # print("token.ttype:", token.ttype)
            # print("token.value:", token.value)

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
                    # print("Set Values:", set_values)

            # 找到 WHERE 子句
            if token.value.upper().startswith("WHERE"):
                # 直接获取 WHERE 子句中的条件部分
                condition = token.value[len("WHERE"):].strip()
                # print("Condition:", condition)
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