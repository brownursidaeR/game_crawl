import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
from datetime import datetime
import re
    
url = 'https://www.9game.cn/kc/'

html = requests.get(url).content.decode('utf-8')
# with open('game.html',encoding='utf-8') as f:
#     html = f.read()
soup = BeautifulSoup( html , 'html.parser') 
table_container = soup.find_all('div', class_='des-table1')  # Locate the 'des-table' div
print(len(table_container))

def parse_detail_info(url):
    if url:
        html = requests.get(url).content.decode('utf-8')
        soup = BeautifulSoup( html , 'html.parser') 
        game_desc = soup.find('p', class_='txt').text.strip()
        developer = soup.find('div', class_='company').text.split('开发者：')[1]
        ul_element = soup.find('ul', class_='focus-img')
        # Extract img src links
        img_links = []
        for li_element in ul_element.find_all('li'):
            img_element = li_element.find('img')
            if img_element:
                img_links.append(img_element['src'])
    else:
        developer = None
        game_desc = None
        screenshots = None
    
    return developer,game_desc,img_links


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

# Process Table Rows
data = []
for table in table_container:
    day = table.find_all('div',class_='day')[0].text
    day = trans_days(day)
    for row in table.find_all('tr'):
        row_data = []
        
        time = row.find('td', class_='timetr').text
        name = row.find('td', class_='nametr').find('a')['title']
        img = row.find('td', class_='nametr').find('img')['xlazyimg']
        page = row.find('td', class_='nametr').find('a')['href']
        developer,game_desc,screenshots = parse_detail_info(page)
        stattr = row.find('td',class_='stattr').text
        game_type = row.find('td',class_='typetr').text
        download = row.find('span', class_=['sbtn icon-qq clientGuide'])['href']
        row_data = ['九游开测表',day,time,name,game_type,'暂无',developer,'暂无',stattr,page,img,'\n'.join(screenshots),game_desc,download]
        # # ['timetr', 'nametr', 'stattr', 'typetr', 'btntr']:
    

        if row_data:  # Only append if there's data
            data.append(row_data)

headers = ['数据来源','测试日期','时间','游戏名','游戏类型','发行厂商','研发厂商','平台评分','测试模式','详情页','icon','图片','游戏介绍','下载链接']
df = pd.DataFrame(data = data,columns=headers)
today = date.today()
df.to_excel('开测九游_{date}.xlsx'.format(date=today),index=False)
print('done')

