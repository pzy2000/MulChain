import pandas as pd
from datetime import datetime

# 读取 CSV 文件的前 20000 行，同时只读取 "timestamp" 和 "transactionHash" 列
df = pd.read_csv('0to999999_BlockTransaction.csv', usecols=['timestamp', 'transactionHash'], nrows=20000)

# 将数据转换为指定格式的列表，并格式化时间戳为 %Y-%m-%d
data_list = [
    {
        'hash': row['transactionHash'],
        'time_stamp': datetime.fromtimestamp(row['timestamp']).strftime('%Y-%m-%d %H_%M_%S')
    }
    for _, row in df.iterrows()
]

# 查看前几个元素
print(data_list[:5])
