import requests,json
from requests_toolbelt.utils import dump
import pandas as pd
import time
from datetime import date

def huawei_crawl(page=1):
    url = "https://store-drcn.hispace.dbankcloud.com/hwmarket/api/clientApi"
    payload = "apsid=1716993673733&arkMaxVersion=0&arkMinVersion=0&arkSupport=0&brand=google&channelId=startFromLauncher&clientPackage=com.huawei.appmarket&cno=4010001&code=0200&contentPkg=&dataFilterSwitch=&deviceId=8e0f89cf3975c2670b303134d75050bd0623f700853a29a046f07082433e1082&deviceIdRealType=4&deviceIdType=9&deviceSpecParams=%7B%22abis%22%3A%22arm64-v8a%22%2C%22deviceFeatures%22%3A%22U%2C1J%2CP%2C1O%2CB%2C0c%2Ce%2Cp%2Ca%2Cb%2C04%2Cm%2C1M%2C08%2C03%2CC%2CS%2C0G%2C1Q%2Cq%2C1F%2CL%2C2%2C6%2CY%2CZ%2C1P%2C1G%2C2L%2C1B%2Cf%2C1%2C07%2C8%2C9%2C2K%2C1H%2C1I%2CO%2CH%2C1K%2C2N%2C0E%2CW%2Cx%2C2J%2CG%2Co%2C06%2C3%2CR%2Cd%2CQ%2Cn%2Cy%2CT%2Ci%2Cr%2Cu%2Cl%2C4%2CN%2CM%2C01%2C09%2CV%2C7%2C5%2C0H%2Cg%2Cc%2CF%2Ct%2C0W%2C1N%2C0X%2Ck%2C00%2Cz%2C19%2CK%2CE%2C02%2CI%2C1E%2CJ%2C1C%2Cj%2CD%2Ch%2C1L%2C05%2C1A%2CX%2Cv%2Ccom.verizon.hardware.telephony.lte%2Ccom.verizon.hardware.telephony.ehrpd%2Candroid.software.telecom%2Candroid.hardware.telephony.subscription%2Ccom.google.android.feature.D2D_CABLE_MIGRATION_FEATURE%2Candroid.hardware.telephony.data%2Ccom.google.android.feature.FIR.PROXIMITY%2Candroid.hardware.sensor.dynamic.head_tracker%2Candroid.software.erofs%2Candroid.software.device_lock%2Ccom.google.android.feature.PIXEL_2017_EXPERIENCE%2Ccom.google.android.feature.PIXEL_2018_EXPERIENCE%2Candroid.hardware.telephony.messaging%2Candroid.software.preview_sdk%2Ccom.google.android.feature.PIXEL_2019_EXPERIENCE%2Candroid.hardware.telephony.calling%2Ccom.google.android.feature.PIXEL_2023_MIDYEAR_EXPERIENCE%2Candroid.software.window_magnification%2Candroid.hardware.telephony.radio.access%2Ccom.google.android.feature.GOOGLE_BUILD%2Cvendor.android.hardware.camera.preview-dis.front%2Ccom.google.android.feature.PIXEL_2022_MIDYEAR_EXPERIENCE%2Candroid.software.ipsec_tunnel_migration%2Ccom.google.android.feature.PIXEL_2021_MIDYEAR_EXPERIENCE%2Candroid.hardware.context_hub%2Ccom.google.android.feature.PIXEL_EXPERIENCE%2Ccom.google.android.feature.GOOGLE_FI_BUNDLED%2Ccom.google.android.feature.PIXEL_2020_MIDYEAR_EXPERIENCE%2Candroid.hardware.telephony.carrierlock%2Ccom.google.android.feature.WELLBEING%2Candroid.software.credentials%2Candroid.hardware.device_unique_attestation%2Candroid.software.device_id_attestation%2Ccom.google.android.feature.AER_OPTIMIZED%2Ccom.google.android.feature.NEXT_GENERATION_ASSISTANT%2Ccom.google.android.feature.PIXEL_2019_MIDYEAR_EXPERIENCE%2Ccom.google.android.apps.dialer.SUPPORTED%2Ccom.google.android.feature.GMS_GAME_SERVICE%2Candroid.software.game_service%2Ccom.google.android.feature.GOOGLE_EXPERIENCE%2Ccom.google.android.feature.EXCHANGE_6_2%2Ccom.google.android.feature.DREAMLINER%2Ccom.google.android.feature.ADAPTIVE_CHARGING%2Ccom.google.android.feature.PIXEL_2020_EXPERIENCE%2Candroid.hardware.telephony.euicc.mep%2Candroid.software.virtualization_framework%2Ccom.google.android.feature.PIXEL_2021_EXPERIENCE%2Candroid.hardware.keystore.app_attest_key%2Ccom.google.android.feature.QUICK_TAP%2Candroid.software.wallet_location_based_suggestions%2Ccom.google.android.feature.PIXEL_2022_EXPERIENCE%2Ccom.google.android.feature.PIXEL_2023_EXPERIENCE%22%2C%22dpi%22%3A480%2C%22glVersion%22%3A%22OpenGL%20ES%203.2%20v1.r48p0-01eac0.0c65d4c6b01b62685ea9822437ed3925%22%2C%22openglExts%22%3A%22%22%2C%22preferLan%22%3A%22zh%2Cen%22%2C%22usesLibrary%22%3A%225%2C6%2C4%2C1s%2CG%2CG%2CG%2CG%2C3%2CA%2C0U%2C9%2C8%2C2%2Cb%2CE%2C7%2Cd%2C0V%2CD%2CB%2CC%2Ccom.vzw.apnlib%2Ccom.android.hotwordenrollment.common.util%2Ccom.google.pixel.camera.services.cameraidremapper%2Cgoogle-ril%2Clibedgetpu_client.google.so%2Clibedgetpu_util.so%2Candroid.telephony.satellite%2Ccom.google.pixel.camera.connectivity%2Ccom.android.omadm.radioconfig%2Ccom.google.pixel.camera.services.lyricconfigprovider%2Clib_jpg_encoder.so%2Ccom.google.android.camera.experimental2023%2ClibOpenCL-pixel.so%2Candroidx.window.extensions%2Clibedgetpu_dba.google.so%2Ccom.google.pixel.camera.connectivity.impl%2Coemrilhook%2Ccom.google.pixel.camera.services.cameraidremapper.impl%2Ccom.google.pixel.camera.services.lyricconfigprovider.impl%2Ccom.google.android.apps.aicore%2Corg.carconnectivity.android.digitalkey.timesync%2Clib_aion_buffer.so%2Clibgxp.so%2Ccom.google.android.dialer.support%2Ccom.google.android.camera.extensions%2Ccom.google.android.hardwareinfo%2Ccom.google.android.camerax.extensions%2Candroidx.window.sidecar%22%7D&fid=0&gaid=61bdbf6f-1f06-4774-8604-3291efd56c6e&globalTrace=null&gradeLevel=0&gradeType=&hardwareType=0&isSupportPage=1&manufacturer=Google&maxResults=25&method=client.getTabDetail&net=1&oaidTrack=-2&osv=14&outside=0&recommendSwitch=1&reqPageNum={}&roamingTime=0&runMode=2&serviceType=0&shellApkVer=0&sid=1716993637041&sign=u90010905i01110220000000000001000a0000000500100000011000000010000070240b0100011001000%40E0915D43D6254D859B3C7BDE3ACD00FC&thirdPartyPkg=com.huawei.appmarket&translateFlag=0&ts=1716993736917&uri=8f63b82901cf4425ba14ff359fee4188%3Faglocation%3D%257B%2522cres%2522%253A%257B%2522lPos%2522%253A0%252C%2522lid%2522%253A%2522903117%2522%252C%2522pos%2522%253A1%252C%2522resid%2522%253A%25228f63b82901cf4425ba14ff359fee4188%2522%252C%2522rest%2522%253A%2522tab%2522%252C%2522tid%2522%253A%2522dist_0b5e464b2b8f4690861aaccb3182dd80%2522%257D%252C%2522ftid%2522%253A%2522dist_7f80bcb4ed24476f9f70ab8290911aca%2522%252C%2522pres%2522%253A%257B%2522lPos%2522%253A1%252C%2522lid%2522%253A%2522903117%2522%252C%2522pos%2522%253A0%252C%2522resid%2522%253A%25228f63b82901cf4425ba14ff359fee4188%2522%252C%2522rest%2522%253A%2522tab%2522%252C%2522tid%2522%253A%2522dist_0b5e464b2b8f4690861aaccb3182dd80%2522%257D%257D%26templateId%3D34850d944e844288a90ef5843d7d40ac%26uiExp1%3D%255B%257B%2522bucketId%2522%253A%252259%2522%252C%2522layerId%2522%253A%2522s54r8w%2522%252C%2522strategyId%2522%253A%2522AA_s54r8w_17%2522%252C%2522type%2522%253A2%257D%252C%257B%2522bucketId%2522%253A%252272%2522%252C%2522layerId%2522%253A%2522saod5e%2522%252C%2522strategyId%2522%253A%2522510573%2522%252C%2522type%2522%253A2%257D%255D%26requestId%3D9a4adcd2bbf44d33bbce8ae066058865&ver=1.1".format(page)
    headers = {
      'User-Agent': "HiSpace##13.4.1.301##google##Pixel 8 Pro",
      'Connection': "Keep-Alive",
      'Accept': "application/json",
      'Accept-Encoding': "application/json",#"br,gzip",
      'sysUserAgent': "Mozilla/5.0 (Linux; Android 14; Build/AP31.240426.023; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.82 Mobile Safari/537.36",
      'Content-Encoding': "text/html;charset=UTF-8",
    #   'network-in': "NWK(time/20240529144216924)",
      'network-vendor': "NWK",
      'net-msg-id': "4ff81d00f41749419fe71ec7d37a0ee6",
    #   'network-out': "NWK(time/20240529144216925)",
      'Content-Type': "application/raw"
    }

    response = requests.post(url, data=payload, headers=headers)
    game_json = json.loads(response.text)
    totalPages = game_json.get('totalPages')
    if totalPages>page:
        # 用decorater 循环获取页面
    res_data = game_json['layoutData']
    game_data = res_data[0]['dataList']
    game_list = []
    for game in game_data:
        row_data = []
        # break
        icon = game.get('icon')
        name = game.get('name')
        detailId = game['detailId'].split('|')[1] 
        developer = game.get('devName')
        game_type = game.get('TAGNAME')
        download = game.get('downloadUrl')
        description = game.get('description') 
        ORDERUSER = game.get('ORDERUSER') #评分
        FIRSTPUBLISHTIME = game.get('FIRSTPUBLISHTIME')
        screenshots = game.get('RECOMMIMG')
        day,test_time = FIRSTPUBLISHTIME.split(' ')
        row_data = ['华为新游预约',day,test_time,name,game_type,developer,None,ORDERUSER,None,detailId,icon,screenshots,description,download]
        if row_data:  # Only append if there's data
            game_list.append(row_data)
    return game_list

for page in range(1,10):
    game_list = huawei_crawl()
    headers = ['数据来源','测试日期','时间','游戏名','游戏类型','发行厂商','研发厂商','平台评分','测试模式','详情页','icon','图片','游戏介绍','下载链接']
    df = pd.DataFrame(data = game_list,columns=headers)
    today = date.today()
    print(today)
    df.to_excel('开测华为_{date}.xlsx'.format(date=today),index=False)
