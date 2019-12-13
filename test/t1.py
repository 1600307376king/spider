import requests
from urllib3 import encode_multipart_formdata
import math
import random
import time

import json
import re
import pandas as pd
import os


def cleaning_vegetable_data(filename):
    f = open("./jd.json", encoding='utf-8')
    res = json.loads(f.read())
    title = res['result']['config']['gloabTitle']
    stores = res['result']['data']
    product_list = []
    for j in range(1, len(stores) - 1):
        for i in res['result']['data'][j]['data'][0]['skuList']:
            product_list.append([i['skuId'], i['skuName'], i['imgUrl'], i['realTimePrice'],
                                 i['basicPrice'], title])
    # sku = res['result']['data'][1]['data'][0]['skuList']
    # vegetables = [[i['skuId'], i['skuName'], i['imgUrl'], i['realTimePrice'],
    #                i['basicPrice'], title] for i in sku]
    df = pd.DataFrame(product_list, columns=['产品ID', '产品名称', '产品图片', '当前价格', '原价', '产品类型'])
    df.to_excel('./' + filename + '.xlsx', index=False)


def get_app_json_data(url, parameters=None):
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
        'Host': 'daojia.jd.com',
        'Connection': 'Keep - Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp / 3.12.1'
    }
    res = requests.get(url, headers)
    if res.status_code == 200:
        res.json()


def comparision_data(st1, st2):
    n = ''
    for i, j in zip(st1, st2):
        if i != j:
            print(n)
            break
        n += i


def get_execl_data(filename):
    df = pd.read_excel(filename)
    df['产品类型'] = df['产品类型'][0].replace('菜场', '')
    df.to_excel('./' + filename, index=False)


def save_images():
    product_file_list = os.listdir('./xlsx')
    n = 0
    for filename in product_file_list:
        images_list = []

        product_df = pd.read_excel('./xlsx/' + filename)
        pd_type = filename.rstrip('.xlsx')

        for j in product_df['产品图片']:
            images_list.append(j)

        for i in images_list:
            n += 1
            # image_file = requests.get(i)
            # if not os.path.exists('./images/' + pd_type):
            #     os.mkdir('./images/' + pd_type)
            # with open('./images/' + pd_type + '/' + i.split('/')[-1], 'wb') as f:
            #     f.write(image_file.content)

    print(n)


def post_web(url):
    data = {
        'image': ('0effc9be56493a08.jpg', open('./0effc9be56493a08.jpg', 'rb').read())
    }
    headers = {

        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    }
    ed = encode_multipart_formdata(data)
    headers['Content-Type'] = ed[1]
    res = requests.post(url, headers=headers, data=ed[0])
    print(res.status_code)


# post_web('http://127.0.0.1:5000/')



headers = {
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'X-USER-TOKEN': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIyMCIsInVzZXJOYW1lIjoiSFgwMDEyMTM4IiwiZXhwIjoxNTY2Mzg3ODA1LCJ1c2VySWQiOiIyMCIsImlhdCI6MTU2NjM3MzQwNX0.9w__2RGncpdMvbiQAmk75ThgPwDaTXF1VyY1xKVs_zFduUEoJ3_6X2q3ZVYsFIpChKeLEWelhwlmMxEP4lU9QA',
    'Origin': 'http://xx.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    'Accept': '*/*',
    # 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarycDnnz7eKalCPv6GJ',
    'Referer': 'http://xx.cn/manager/', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'}

url = 'http://127.0.0.1:5000/'

data = {
    'type': 0,
    'goodsname': '大青芒果约500g',
    'marketprice': 12,
    'productprice': 15,
    'virtual': 0,
    'virtualsend': 0,
    'dispatchtype': 0,
    'dispatchid': 0,
    'status': 1,
    'isstatustime': 1,
    'statustime[start]': '2019-12-14 00:26',
    'statustime[end]': '2020-01-14 00:26',
    'total': 100,
    'totalcnf': 0,
    'optionArray': {"option_stock":[],"option_id":[],"option_ids":[],"option_title":[],"option_presellprice":[],"option_marketprice":[],"option_productprice":[],"option_costprice":[],"option_goodssn":[],"option_productsn":[],"option_weight":[],"option_virtual":[]}


}

files = {'attach': ('0effc9be56493a08.jpg', open('./0effc9be56493a08.jpg', 'rb'))}
r = requests.post(url, headers=headers, files=files)
print(requests.Request('POST', url, headers=headers, files=files).prepare().body.decode(
    'ascii'))  # 打印字段名和类型
print(r.text)