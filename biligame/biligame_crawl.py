import requests
from bs4 import BeautifulSoup
import pandas as pd
import json,time
from datetime import date

page_num = 1
page_size = 20
url = "https://le3-api.game.bilibili.com/pc/game/ranking/page_start_test_list?page_num={}&page_size={}&x-fix-page-num=1".format(page_num,page_size)

payload = {}
headers = {
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'cookie': 'b_nut=1713748898; _uuid=2C85DC107-A14D-3236-4424-D82109124BD5298521infoc; buvid3=53350458-2582-517E-B371-43ED63851EDD02763infoc; buvid4=ACDC1F14-FC4E-9150-85EE-AFE4A2C1B5E002763-024042201-FCnGo9iCyCM%2Bq2Hw4cxsag%3D%3D; buvid_fp_plain=undefined; rpdid=|(J|~uR|Ju~Y0J\'u~uRuuklY~; LIVE_BUVID=AUTO1317142909228219; PVID=1; CURRENT_FNVAL=4048; fingerprint=61c216dd1db6e787c01224a4585c227e; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTcxNDU3ODIsImlhdCI6MTcxNjg4NjUyMiwicGx0IjotMX0.JRmlaWt7qG2dvy4RAxCo2gIoSqay8169V8JODYjlGlQ; bili_ticket_expires=1717145722; sid=8n399ubu; share_source_origin=COPY; bsource=search_google; b_lsid=4810942F4_18FC3501112; buvid_fp=53350458-2582-517E-B371-43ED63851EDD02763infoc',
  'origin': 'https://game.bilibili.com',
  'priority': 'u=1, i',
  'referer': 'https://game.bilibili.com/',
  'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}

# biligame response
response = requests.request("GET", url, headers=headers, data=payload)


def get_screenshot(game_id):
    url = 'https://line1-h5-pc-api.biligame.com/game/detail/content?game_base_id={}'.format(game_id)
    res = requests.get(url)
    screen_shots = json.loads(res.text).get('data').get('screen_shots')
    screenshots = [i.get('url') for i in screen_shots]
    return screenshots
# print(response.text)

def timestamp_to_time(timeStamp,time_format_string):
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime(time_format_string, timeArray)
    return otherStyleTime

# with open('bili_game.json',encoding='utf-8') as f:
#     game_json = f.read()

# html = requests.get(url).content.decode('utf-8')
info = json.loads(response.text)
data = info.get('data')
game_list = []

if data:
    for game in data:
        row_data = []
        title = game['title']
        developer_name = game['developer_name'] # 发行
        establisher_name = game['establisher_name'] # 研发
        game_name = game['game_name']
        game_base_id = game['game_base_id']
        screenshots = get_screenshot(game_base_id)
        start_test_time = int(game['start_test_time'])/1000
        start_test_type = game['start_test_type'] #测试模式
        icon = 'https:'+game['icon']
        game_detail_link = game['game_detail_link']
        download_link = game.get('android_download_link')
        category_name = game['category_name']
        grade = game['grade']
        game_desc = game['game_desc']
        day = timestamp_to_time(start_test_time,"%Y-%m-%d")
        test_time = timestamp_to_time(start_test_time,"%H:%M")
        row_data = ['bili开测表',day,test_time,game_name,category_name,developer_name,establisher_name,grade,start_test_type,game_detail_link,icon,'\n'.join(screenshots),game_desc,download_link]
        if row_data:  # Only append if there's data
            game_list.append(row_data)


headers = ['数据来源','测试日期','时间','游戏名','游戏类型','发行厂商','研发厂商','平台评分','测试模式','详情页','icon','图片','游戏介绍','下载链接']
df = pd.DataFrame(data = game_list,columns=headers)


today = date.today()
df.to_excel('开测bili_{date}.xlsx'.format(date=today),index=False)
print('done')
