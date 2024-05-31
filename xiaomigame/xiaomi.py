import requests

url = "https://app.knights.mi.com/knights/recommend/simple/page/normal/v7"

payload = "availableSpace=12719887360&channel=meng_1449_55_android&id=90028&lastGameId=0&manufacturer=Google&mgid=game_86bad04acdd1a24484e94c5a8d87db36&model=Pixel+8+Pro&page=1&pageSize=10&platform=android&recommend=true&remoteIp=192.168.50.249&sdk=34&supportTmpfs=false&totalSpace=30712801792&ua=Google%7CPixel+8+Pro%7CAP31.240426.023%7C34%7Chusky&uuid=0&versionCode=130500020&versionName=13.5.0.20"

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

response = requests.post(url, data=payload, headers=headers)

print(response.text)