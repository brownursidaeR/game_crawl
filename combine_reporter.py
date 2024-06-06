from datetime import date
import pandas as pd
import glob2

today = date.today()
file_list = glob2.glob('./*game/*_{}.xlsx'.format(today))
print(file_list)


# 读取现有 Excel 文件
existing_data = pd.read_excel('近期测试预约产品.xlsx')

def process_new_data_file(file_path):
    """
    读取新数据文件，删除重复项并将其与现有数据合并。

    参数：
        file_path：新数据文件的路径

    返回：
        合并后的非重复数据 DataFrame
    """
    print(file_path)
    # 读取新数据
    new_data = pd.read_excel(file_path)

    # 删除重复项
    new_data.drop_duplicates(inplace=True)

    # 合并数据
    data = pd.concat([existing_data, new_data], ignore_index=True)

    # 删除重复项
    data.drop_duplicates(inplace=True)

    return data

# 循环处理每个文件
for file_path in file_list:
    data = process_new_data_file(file_path)

    # 更新现有数据
    existing_data = data.copy()

# 将数据写入现有 Excel 文件
existing_data = existing_data.sort_values(by=['测试日期', '时间','游戏名'], ascending=True)
# Output the sorted DataFrame
##print(sorted_data)
existing_data.to_excel('近期测试预约产品.xlsx', index=False)
print('done')
