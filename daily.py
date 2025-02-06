import json
import pandas as pd
import time
from datetime import date
import requests
import urllib.parse
# REF https://github.com/Asoul/tsrtc 



targets=['1101','1102']

endpoint = 'https://mis.twse.com.tw/stock/api/getStockInfo.jsp'
# Add 1000 seconds for prevent time inaccuracy
dtime= date.today().strftime('%Y%m%d')
channels = '|'.join('tse_{}.tw_{}'.format(target, dtime) for target in targets)
url='{}?ex_ch={}'.format(endpoint, channels)
print(url)


req = requests.session()
req.get('http://mis.twse.com.tw/stock/index.jsp',
        headers={'Accept-Language': 'zh-TW'})
response = req.get(url)
content = json.loads(response.text)
pd.DataFrame( content['msgArray'])


ga_list=content['msgArray']
names_key = { 'c': '股票代號' ,
             'z':'最近成交價',
            }

for row in ga_list:
    for k, v in names_key.items():
        for old_name in row:
            if k == old_name:
                row[v] = row.pop(old_name)

pd.DataFrame(ga_list)
