from datetime import datetime

# 定义时间戳
timestamp = 1538502669

# 将时间戳转换为日期时间格式
date_time = datetime.fromtimestamp(timestamp)

# 显示年月日
print(date_time.strftime('%Y-%m-%d'))
