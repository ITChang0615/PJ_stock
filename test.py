import requests
from bs4 import BeautifulSoup
import pandas as pd
import warnings
import json

warnings.filterwarnings("ignore")


url = 'https://ic.tpex.org.tw/index.php'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'    
}
proxies = {
    "http": "http://itchang:B$0000000000@auhqwsg.corpnet.auo.com:8080",
    "https": "http://itchang:B$0000000000@auhqwsg.corpnet.auo.com:8080"
}

def abs_url(url, base):
    # 取得完整 URL
    if url is None:
        return None
    return url if url.startswith('http') else base + '/' + url.lstrip('/')

def clean(txt):
    return txt.strip().replace('\n', ' ').replace('\r', '').replace('\t', ' ') if txt else ''

url = "https://ic.tpex.org.tw/index.php"   # 這裡請換成你要抓取的實際 URL
response = requests.get(url,  headers=headers,verify=False, proxies=proxies, timeout=15)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')


data = []
base_url = url.split('/')[0] + "//" + url.split('/')[2]


main = soup.select('.Content_2 .item')
for a in main:
    a_tag = a.find('a')

    href = a_tag['href'] if a_tag else ''
    abs_href = abs_url(href, base_url)
    title = clean(a.find(class_='txt').get_text())

    subtitle = ''
    item = ''
    
    ul = a.find('ul')
    if ul:
        sub1 = ul.select('.listItem a')
        for b in sub1:
            href2 = b['href'] if b.has_attr('href') else ''
            url2 = abs_url(href2, base_url)
            spans = b.select('span')
            subtitle = clean(spans[1].get_text()) if len(spans) > 1 else ''
            
            third_menu = b.find(class_='thirdMenu')
            if third_menu:
                sub2 = third_menu.select('.itemLink')
                for c in sub2:
                    onclick = c.get('onclick')
                    if onclick:
                        # 取出 URL
                        url3 = onclick.replace("location.href=", "").replace("'", "")
                        url3 = abs_url(url3, base_url)
                    else:
                        url3 = ''
                    item = clean(c.get_text())
                    data.append({'title': title, 'subtitle': subtitle, 'item': item, 'url': url3})
            else:
                data.append({'title': title, 'subtitle': subtitle, 'item': item, 'url': url2})
    else:
        data.append({'title': title, 'subtitle': subtitle, 'item': item, 'url': abs_href})

areadata=[]
detaildata=[]
origin='https://ic.tpex.org.tw/'

# 第二階處理
for s_data in data[0:1]:
    response = requests.get(s_data['url'],  headers=headers,verify=False, proxies=proxies, timeout=15)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.select('div'))
    # 取 maintitle、subtitle
    for chain in soup.select('.chain'):
        area = chain.select_one('.chain-title-panel').get_text(strip=True)
        for b in chain.select('.company-chain-panel'):
            title = clean(b.get_text())
            areadata.append({'area': area, 'title': title})
    
    # 取 dialog
    
    for a in soup.select('.ui-dialog'):
        title = a.select_one('.ui-dialog-title').get_text(strip=True)
        for b in a.select('.company-text-over'):
            name = b.get_text(strip=True)
            href = b.get('href') or ''
            url = abs_url(href, origin)
            try:
                number = href.split('stk_code=')[1]
            except Exception:
                number = ''
            area = next((x['area'] for x in areadata if x['title'] == title), '')
            data.append({'area': area, 'title': title, 'number': number, 'name': name, 'url': url})

    



json_str = json.dumps(areadata, ensure_ascii=False, indent=2)
print('✅ 產出結果 ↓')
print(len(areadata))
# print(json_str)
# 這裡沒有 copy(json) 等功能，請自行複製輸出結果
with open('output.json', 'w', encoding='utf-8') as f:
    f.write(json_str)
