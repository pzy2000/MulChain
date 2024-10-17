import os
import json
from datetime import datetime
from tqdm import tqdm
import pickle  # 导入 pickle 模块

root_dir = '../bitcoin'

# 创建一个空的列表来保存提取的文件路径
file_list = []

# 使用 os.walk 将所有 .json 文件路径添加到 file_list
for root, dirs, files in os.walk(root_dir):
    for file in files:
        # 检查文件是否以 .json 结尾
        if file.endswith('.json'):
            # 获取完整文件路径并添加到列表
            file_path = os.path.join(root, file)
            file_list.append(file_path)

# 创建一个空的列表来保存提取的结果
data_list = []

# 遍历文件列表，添加进度条显示
for file_path in tqdm(file_list, desc="Processing JSON files"):
    # 打开并读取 JSON 文件内容
    with open(file_path, 'r') as f:
        try:
            json_data = json.load(f)

            # 检查 json_data 是否为列表
            if isinstance(json_data, list):
                # 迭代列表中的每个元素
                for item in json_data:
                    # 提取 "hash" 和 "time_stamp" 信息
                    file_hash = item.get('hash', None)
                    time_stamp = item.get('time_stamp', None)

                    # 检查是否成功提取
                    if file_hash and time_stamp:
                        # 转换 time_stamp 列表为时间字符串
                        time_stamp_str = datetime(*time_stamp).strftime('%Y-%m-%d %H:%M:%S')

                        # 保存到结果列表
                        data_list.append({
                            'hash': file_hash,
                            'time_stamp': time_stamp_str
                        })
            else:
                print(f"Unexpected JSON structure in file: {file_path}")

        except json.JSONDecodeError:
            print(f"Error decoding JSON from file: {file_path}")

print(f"Total JSON files processed: {len(data_list)}")

# 使用 pickle 将 data_list 保存到文件中
with open('data_list.pkl', 'wb') as f:
    pickle.dump(data_list, f)
