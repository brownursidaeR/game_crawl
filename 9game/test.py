from datetime import datetime
from dateutil import parser
import re

date_str = "06月28日"

def trans_days(date_str):
    match = re.match(r'(\d+)月(\d+)日', date_str)
    if match:
        month = int(match.group(1))
        day = int(match.group(2))

        # 创建一个 datetime 对象，并设置年份为2024年
        parsed_date = datetime(year=datetime.today().year, month=month, day=day)

        # 格式化为目标字符串格式
        formatted_date = parsed_date.strftime("%Y-%m-%d")

    return formatted_date

print(trans_days(date_str))
