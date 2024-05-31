import requests,json,time,re
import pandas as pd
from datetime import date
from datetime import datetime

def trans_days(date_str):
    match = re.match(r'(\d+)月(\d+)日', date_str)
    if match:
        month = int(match.group(1))
        day = int(match.group(2))

        # 创建一个 datetime 对象，并设置年份为2024年
        parsed_date = datetime(year=datetime.today().year, month=month, day=day)

        # 格式化为目标字符串格式
        formatted_date = parsed_date.strftime("%Y-%m-%d")
    else:
        formatted_date = None
    return formatted_date

def get_info(app_id):
    url = 'https://www.taptap.cn/webapiv2/app/v4/detail?id={}&X-UA=V%3D1%26PN%3DWebApp%26LANG%3Dzh_CN%26VN_CODE%3D102%26LOC%3DCN%26PLT%3DPC%26DS%3DiOS%26UID%3Dab7e0d69-2499-43b7-beb1-090c8c8865b7%26OS%3DWindows%26OSV%3D10%26DT%3DPC'.format(app_id)
    payload = {}
    headers  = {
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cookie': 'web_app_uuid=ab7e0d69-2499-43b7-beb1-090c8c8865b7; _ga=GA1.1.1418481923.1713862453; _clck=1eh5u5x%7C2%7Cfm8%7C0%7C1577; XSRF-TOKEN=7ka6i37fql1ex2o3lgms; locale=zh_CN; apk_download_url_postfix=/seo-google_games; tap_theme=; _clsk=1ug71jb%7C1717124012850%7C39%7C0%7Cs.clarity.ms%2Fcollect; _ga_LX4W0NH3WZ=GS1.1.1717128808.2.0.1717128808.60.0.0; acw_tc=2760820317171355837625289eb8d3bd0526b3676cc240b9ba6e879c904642; _ga_6G9NWP07QM=GS1.1.1717135583.24.1.1717135609.0.0.0; ssxmod_itna=QuitiKGKBKDKzDl3x+obH7SDWq0Ivwxd3No3D/AB+D3q0=GFDt4iAABeDC8+t8t0EhUPAez4rqaqabEm5WPBQDpRzW3ex0aDbMcGqrnPxiiDC8KDIDWeDiDG+ODFxYoDervQDF8NVz/9IEPDQ4GyDitDKLp9tG+K8qUKDDXKjnbRlGqDbE=MBS0FbeDSK0tv8qDMD7tD/3hFEA=DGua7EGNMQcE=rOI4deGuDG=KEMpex0PBlqNR9nveirhYSgG2BiprnEGe87DNbB+4Kivql7x0OOGK3rY1B/+fpXxDGSrdlB4xD===; ssxmod_itna2=QuitiKGKBKDKzDl3x+obH7SDWq0Ivwxd3XxG9tE8tDBkm47p6KXBxPf9wBIB+F/Dn+Q35FeQK2OSm6nTRpWBnREQDBWaoNGqIPdLQsYg6eBizYZ3mTQPrZtiMugPkeaKchPc6NIzpmOel+ohMF8EqPqjFeRdsRbAe9+r94jRc0f25LC2YgxRKdTThK6uzfenWr=bNPPaG3PcEYQFL/gci6CE0iPEe1dhC2absknKs+6GOcrAP/43+FlyaQIYsmgypTUr333IsXSL7stMwO629nacjlxke8E=EXblxlGjOom+z=TdjE8riOr70syi7TLGZRCqe3ffe8rTdSYPeGu4Ydf+PxoqlGubGzC5sx5ohNR25lieijiZgdCGqRr+0ldZ4ksebnmrU+TeWaBwkjMPuRPfb7tjoA+qvDDwo44F=PjQwCpTt+=3qAtwqQcj4Tj6G97mPWtNBhIAr0zmRpRvfcsWUES4XgI9FDcSxDjKDeLx4D==; tfstk=fi6ogy2Tl_R5VnoLrtv73xqzHdFvN49BJwHpJpLUgE8jy4HRYHJhAGrWJMz5tZj1leLzRL3FtZ_bV9BhAvxFYwZWJuNAVg9BLPUOKRI5VD6wvPr9TIoVc30P2z0NRg9BLrhgWnKhVNflJcUkLov2xHlyLUJE0oxHjeJezBuqgh828pJF8nJ2bHLEz3lruqlfSv8GLt64Xf7gdjjCGtxkg5Iyu61Lv3duygYxLPWDqPTN4EDELUOAkBjc2zD1DL6hShQ83YbGft_D0Ny3op_fTw-huRgpF1Q5CIAjxvbMEwANUImELKJXuKxVQkh6ktYR8TA4XAApnOdMUsFbPBpyjwW5rDDF7iIOFI63Sq8Cwh92XgwondSyYgRKgf-1dvt4vtlIOQ-XmFaV6F8-brY6Soqm17Oyc3UTmocIOQ-XmFE0mfgBant8W',
    'priority': 'u=1, i',
    'referer': 'https://www.taptap.cn/top/reserve?page=3',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)
    game_detail = data['data']
    screenshots = [i['original_url'] for i in game_detail['screenshots']]
    information = game_detail.get('information')
    info_dict = {item.get('title'): item.get('text') for item in information}
    manufacturer_name = info_dict.get("厂商")
    supplier_name = info_dict.get("供应商")
    developer = supplier_name
    return developer,screenshots

def tap_crawler(page_num):
    url = "https://www.taptap.cn/webapiv2/app-top/v2/hits?from={}&limit=10&type_name=reserve&X-UA=V%3D1%26PN%3DWebApp%26LANG%3Dzh_CN%26VN_CODE%3D102%26LOC%3DCN%26PLT%3DPC%26DS%3DiOS%26UID%3Dab7e0d69-2499-43b7-beb1-090c8c8865b7%26OS%3DWindows%26OSV%3D10%26DT%3DPC".format(page_num)
    print(url)
    payload = {}
    headers  = {
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cookie': 'web_app_uuid=ab7e0d69-2499-43b7-beb1-090c8c8865b7; _ga=GA1.1.1418481923.1713862453; _clck=1eh5u5x%7C2%7Cfm8%7C0%7C1577; XSRF-TOKEN=7ka6i37fql1ex2o3lgms; locale=zh_CN; apk_download_url_postfix=/seo-google_games; tap_theme=; _clsk=1ug71jb%7C1717124012850%7C39%7C0%7Cs.clarity.ms%2Fcollect; _ga_LX4W0NH3WZ=GS1.1.1717128808.2.0.1717128808.60.0.0; acw_tc=2760820317171355837625289eb8d3bd0526b3676cc240b9ba6e879c904642; _ga_6G9NWP07QM=GS1.1.1717135583.24.1.1717135609.0.0.0; ssxmod_itna=QuitiKGKBKDKzDl3x+obH7SDWq0Ivwxd3No3D/AB+D3q0=GFDt4iAABeDC8+t8t0EhUPAez4rqaqabEm5WPBQDpRzW3ex0aDbMcGqrnPxiiDC8KDIDWeDiDG+ODFxYoDervQDF8NVz/9IEPDQ4GyDitDKLp9tG+K8qUKDDXKjnbRlGqDbE=MBS0FbeDSK0tv8qDMD7tD/3hFEA=DGua7EGNMQcE=rOI4deGuDG=KEMpex0PBlqNR9nveirhYSgG2BiprnEGe87DNbB+4Kivql7x0OOGK3rY1B/+fpXxDGSrdlB4xD===; ssxmod_itna2=QuitiKGKBKDKzDl3x+obH7SDWq0Ivwxd3XxG9tE8tDBkm47p6KXBxPf9wBIB+F/Dn+Q35FeQK2OSm6nTRpWBnREQDBWaoNGqIPdLQsYg6eBizYZ3mTQPrZtiMugPkeaKchPc6NIzpmOel+ohMF8EqPqjFeRdsRbAe9+r94jRc0f25LC2YgxRKdTThK6uzfenWr=bNPPaG3PcEYQFL/gci6CE0iPEe1dhC2absknKs+6GOcrAP/43+FlyaQIYsmgypTUr333IsXSL7stMwO629nacjlxke8E=EXblxlGjOom+z=TdjE8riOr70syi7TLGZRCqe3ffe8rTdSYPeGu4Ydf+PxoqlGubGzC5sx5ohNR25lieijiZgdCGqRr+0ldZ4ksebnmrU+TeWaBwkjMPuRPfb7tjoA+qvDDwo44F=PjQwCpTt+=3qAtwqQcj4Tj6G97mPWtNBhIAr0zmRpRvfcsWUES4XgI9FDcSxDjKDeLx4D==; tfstk=fi6ogy2Tl_R5VnoLrtv73xqzHdFvN49BJwHpJpLUgE8jy4HRYHJhAGrWJMz5tZj1leLzRL3FtZ_bV9BhAvxFYwZWJuNAVg9BLPUOKRI5VD6wvPr9TIoVc30P2z0NRg9BLrhgWnKhVNflJcUkLov2xHlyLUJE0oxHjeJezBuqgh828pJF8nJ2bHLEz3lruqlfSv8GLt64Xf7gdjjCGtxkg5Iyu61Lv3duygYxLPWDqPTN4EDELUOAkBjc2zD1DL6hShQ83YbGft_D0Ny3op_fTw-huRgpF1Q5CIAjxvbMEwANUImELKJXuKxVQkh6ktYR8TA4XAApnOdMUsFbPBpyjwW5rDDF7iIOFI63Sq8Cwh92XgwondSyYgRKgf-1dvt4vtlIOQ-XmFaV6F8-brY6Soqm17Oyc3UTmocIOQ-XmFE0mfgBant8W',
    'priority': 'u=1, i',
    'referer': 'https://www.taptap.cn/top/reserve?page=3',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    game_json = response.text
    # print(game_json)
    game_list = json.loads(game_json)['data']['list']
    row_data = []
    for game in game_list:
        is_ad = game.get('is_ad')
        app = game.get('app')
        id = game.get('app').get('id')
        page = 'https://www.taptap.cn/app/'+str(id)
        title = app.get('title')
        icon = app.get('icon').get('original_url')
        download_site = app.get('uri').get('download_site')
        down_apple = app.get('uri').get('apple')
        down_google = app.get('uri').get('google_play') 
        hints = app.get('hints') # ["限量测试已开启"]
        if hints:
            if '月' in str(hints):
                day = trans_days(hints[0].split(' ')[0])
            else:
                day = None
        else:
            day = None
        stat = app.get('stat')
        score = stat.get('rating').get('score')
        reserve_count = stat.get('reserve_count')
        feed_count = stat.get('feed_count')
        ad_banner = app.get('ad_banner').get('url')
        top_banner = app.get('top_banner').get('url')
        banner = app.get('banner').get('url')
        tag = [i['value'] for i in app.get('tags')] # 游戏标签
        desc = app.get('description').get('text')
        developer,screenshots = get_info(id)
        row_data = ['tap预约表',day,None,title,tag,'暂无',developer,score,hints,page,icon,'\n'.join(screenshots),desc,'\n'.join([download_site,down_apple,down_google])]
        if row_data:  # Only append if there's data
            data.append(row_data)
    return data

data = []
all_dfs = []
# 调用函数并打印结果
for page in range(0, 16):
    page_num = page*10
    data = tap_crawler(page_num)
    df_headers = ['数据来源','测试日期','时间','游戏名','游戏类型','发行厂商','研发厂商','平台评分','测试模式','详情页','icon','图片','游戏介绍','下载链接']
    df = pd.DataFrame(data = data,columns=df_headers)
    # df.to_excel('{}.xlsx'.format(page_num))
    time.sleep(0.5)
all_dfs.append(df)

today = date.today()
final_df = pd.concat(all_dfs, ignore_index=True)
final_df.to_excel('开测tap_{date}.xlsx'.format(date=today),index=False)