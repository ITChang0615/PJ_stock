import json
import pandas as pd
import time
from datetime import date
import requests
import urllib.parse
global df_RunRealTimeStock
df_RunRealTimeStock=pd.DataFrame()
# REF https://github.com/Asoul/tsrtc 
#https://hackmd.io/@LinPolly/ByCvwhUOh


def get_stock_info():
    file_path='StockBaseData.csv'
    df=pd.read_csv(file_path)
    df=df.dropna()
    df['公司代號']=df['公司代號'].astype(int).astype(str)
    
    # return list(_baseInfo.dropna()['公司代號'][:50])
    return df.drop_duplicates()

def get_Url(targets,type_tse_otc):
    
    endpoint = 'https://mis.twse.com.tw/stock/api/getStockInfo.jsp'
    # Add 1000 seconds for prevent time inaccuracy
    dtime= date.today().strftime('%Y%m%d')
    if type_tse_otc=='tse':
        channels = '|'.join('tse_{}.tw_{}'.format(target, dtime) for target in targets)
    else:
        channels = '|'.join('otc_{}.tw_{}'.format(target, dtime) for target in targets)
    url='{}?ex_ch={}'.format(endpoint, channels)
    
    return url


def batch_size(data_list, batch_size):
    x=[]
    # 計算總共需要多少個批次
    num_batches = (len(data_list) + batch_size - 1) // batch_size
    
    # 迴圈遍歷每個批次
    for i in range(num_batches):
        start_index = i * batch_size
        end_index = min((i + 1) * batch_size, len(data_list))
        x.append(data_list[start_index:end_index])
        
    return x


def get_requests():
    req = requests.session()
    req.get('http://mis.twse.com.tw/stock/index.jsp',headers={'Accept-Language': 'zh-TW'})
    return  req
    
def craw_realtime_stock(url,req):

    response = req.get(url)
    content = json.loads(response.text)
    return content['msgArray']

    
def processing_data_to_df(json):
    # process data
    ga_list=json
    names_key = { 'c': 'Stock' ,
                 'z':'Price',
                 'nf':'Company',
                 'g':'揭示買量',
                 'b':'揭示買價',
                 'a':'揭示賣價',
                 'f':'揭示賣量',
                 'v':'累積成交量',
                }
    cols=[value for key, value in names_key.items()]
    for row in ga_list:
        new_row = {}  # 创建新字典
        for old_name, value in row.items():  # 遍历旧字典
            new_name = names_key.get(old_name, old_name)  # 替换键名
            new_row[new_name] = value  # 赋值到新字典
        row.clear()  # 清空原字典
        row.update(new_row)  # 用新字典更新原字典
        
    df= pd.DataFrame(json)[cols]   
    df=df[pd.notna(df['Company'])]
    for x in ['揭示賣價','揭示買價','揭示賣量','揭示買量']:
        df[x]=df[x].str.split('_', 1).str[0]
    
    return df

def get_craw_url(data,size):
    x=[]
    # tse 上市
    targets=data[data['Type'] == '上市'].dropna()['公司代號']
    for i in batch_size(list(targets),size):
        x.append(get_Url(i,'tse'))
        
    # otc 上櫃
    targets=data[data['Type'] != '上市'].dropna()['公司代號']
    for i in batch_size(list(targets),size):
        x.append(get_Url(i,'otc'))
        
    return x


_baseInfo=get_stock_info()
urllist=get_craw_url(_baseInfo,60)
req=get_requests()


urllist[1]




for url in urllist:
    jsondata=craw_realtime_stock(url,req)
    df=processing_data_to_df(jsondata)
    global df_RunRealTimeStock  
    if  df_RunRealTimeStock.empty:
        df_RunRealTimeStock=df
    else :
        df_RunRealTimeStock = pd.concat([df_RunRealTimeStock, df], ignore_index=True)
    time.sleep(4)     




df_RunRealTimeStock
