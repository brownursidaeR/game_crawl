import requests,json
from datetime import date
import pandas as pd

proxies = {
    'http': 'http://127.0.0.1:7897',
    'https': 'http://127.0.0.1:7897'  # https -> http
}


def mi_detail(game_id):
    url = "https://app.knights.mi.com/ginfo/api/m/detail/page"

    payload = "gameId={}".format(game_id)

    headers = {
        'User-Agent': "okhttp/4.9.3",
        'Accept-Encoding': "gzip",
        'cache-control': "no-cache",
        'content-type': "application/x-www-form-urlencoded; charset=utf-8",
        'mi-game-center-pi': "IlfybC17sMEcqZHeze00yNiJ9rPXtRzEAWAPu2wWOGg3F/ZP8/FJ9F3x7mfJMo83H76Pl9myob+NTbfHnG9knnvnLayhFDgh7DDiE2xxo+5fiVKYEATH5A5NJYgye4GDprL/qaYgrkpGqkZ88KdSY6WC0J/VBr+JA9tZ7vm5iN9g4T1MB+d1zUuOyOrQ7sxq3ZVjkMaDBYMZaP+drnmVkqKfrlhcyVNfnBs/Zh3SU+9hHXI5TB67WorC5xmo2pIq8eM0lSYu6tN9aDq2+8QlTUOZiakPxoaBptifL7RT7ME4mKv7ONy5wTHOkCj99nDr4P81ga88H875wjQ02pGIBCDeM8+TeEHBwOzJ54EkA/V+qPkcAuVGy8TbMMMJCRLD3oWAZz1xAgAyVbpev7YFx+LQqU4VDKBesNTpKaOyd4944nvMsGHYVupNHPsDb1Tw7gSbOKLV0SL5f1uK6676K1d8Je7ASFFCeQebEtQ2iKxZhOQf9wINepV6AS4fiyZaJSfvrw8VM07rSujHTFzMj68xWIDflGpp1HKPEh18k7PaOjS8DDJjkq16axIve9E7Rg9TC/GYbqn8O45kRKo31KFXkxUXmeIHR0mYNtwUHdkbdLz2gQbZtzKBdsqM/7/d+kZ/L7s+piUHdd/PKalrPeoydYxb0m2NmA3Cdqk0kQI=",
        'mi-game-center-onceid': "a62c592b-4ec0-4330-8eea-3babefdbb1f6",
        'mi-game-center-incid': "56",
        'mi-game-first': "1716990582072",
        'mi-game-versiontype': ""
    }

    response = requests.post(url, data=payload, headers=headers,proxies=proxies)

    print(response.text)
    return

def mi_crawl(page=1):
    while True:
          url = "https://app.knights.mi.com/knights/recommend/simple/page/normal/v7"

          payload = "availableSpace=12719887360&channel=meng_1449_55_android&id=90028&lastGameId=0&manufacturer=Google&mgid=game_86bad04acdd1a24484e94c5a8d87db36&model=Pixel+8+Pro&page={}&pageSize=10&platform=android&recommend=true&remoteIp=192.168.50.249&sdk=34&supportTmpfs=false&totalSpace=30712801792&ua=Google%7CPixel+8+Pro%7CAP31.240426.023%7C34%7Chusky&uuid=0&versionCode=130500020&versionName=13.5.0.20".format(page)

          headers = {
              'User-Agent': "okhttp/4.9.3",
              'Accept-Encoding': "gzip",
              'cache-control': "no-cache",
              'content-type': "application/x-www-form-urlencoded; charset=utf-8",
              'mi-game-center-pi': "m59Ft9QdOlrCA14gQoQXyutnhvFhMRMOod2g8ZAFjCUDIAxGnydy047hC4jHDFEJgmbHloBZMzg9ZbdfG7Vk3qqvIrzKXU0uchdsmxNZ7xfwPICNbxWOOm82tbhgfDswEomvkc8FMfuczxTE6g/ckaQCqDJEfESONvTbG6EB23qeyumNvPV/v9nU0b1ui2ELaYI4OcSDQz0iCZdp6zaJqQvtffVrJXjiA8yBT3dt68gJ5PCHIE+APVUFuWbAJFrj++BR8bYIKXTWFurRYwljb86RtGphTpFlTTpOI1S9G/lWBPF5uDP+PVda/+Puu2t744SofNcUn3rYOYFKzLMR3GTiUoqzLpqofaZgafBX/4gKEeRgQsNuPcU82/3ACKwD95QnwwrechZCkdpA13vaF2GClvpO7JZ8iJ3n9SiXiAmN69YnuYlwsw2n9GN/gCjMKTI2cmHhpNcdmgQg/b17ocy1gJ5f03mhNy9zJIzyQGD2A7L/dhqj/6qdXTHS8bmBaqXbaMTodRrWqE4nlUj9FOYnfKr0f6E7TZbwT0gMhqA0K5ED50P/UbsQz5cMtXHR1Y+2Et+Q0HyKKuI1i0OQEU+vmpFwUEA0M7qMqQQuIrls/QF23m7jJTBOQMBjETr98MbINqgxhpcosn9wyX40P6TkwutjMK+0W/47KPTNJyY=",
              'mi-game-center-onceid': "56442df5-2a2a-4b67-951c-70feab8ee783",
              'mi-game-center-incid': "49",
              'mi-game-first': "1716990582072",
              'mi-game-versiontype': ""
          }

          response = requests.post(url, data=payload, headers=headers, proxies=proxies)
          game_json = json.loads(response.text)
          isLastPage = game_json.get('data').get('isLastPage')
          if isLastPage:
              print(isLastPage)

              #代码
              break
          game_list = game_json.get('data').get('blocks')
          if game_list:
            for game in game_list:
              print(game.get('title'))
          page+=1
    return all_df

all_df = []
today = date.today()
print(today)
all_df = mi_crawl()
# all_df = pd.concat(all_df, ignore_index=True)
# all_df.to_excel('开测小米_{date}.xlsx'.format(date=today), index=False)