import requests
from urllib3 import encode_multipart_formdata
import math
import random
import time

import json
import re
import pandas as pd
import os
import pymysql


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

def post_img():
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
        'optionArray': {"option_stock": [], "option_id": [], "option_ids": [], "option_title": [],
                        "option_presellprice": [], "option_marketprice": [], "option_productprice": [],
                        "option_costprice": [], "option_goodssn": [], "option_productsn": [], "option_weight": [],
                        "option_virtual": []}

    }

    files = {'attach': ('0effc9be56493a08.jpg', open('./0effc9be56493a08.jpg', 'rb'))}
    r = requests.post(url, headers=headers, files=files)
    print(requests.Request('POST', url, headers=headers, files=files).prepare().body.decode(
        'ascii'))  # 打印字段名和类型
    print(r.text)


def connection_mysql(db, cursor, product_type, product_name, product_image, product_price, product_cur_price, inventory):
    sql = '''
        insert into ims_ewei_shop_goods(`uniacid`, `pcate`, `ccate`, `type`, `status`, `displayorder`, `title`, `thumb`, `unit`, `description`, `content`, `goodssn`, `productsn`, `productprice`, `marketprice`, `costprice`, `originalprice`, `total`, `totalcnf`, `sales`, `salesreal`, `spec`, `createtime`, `weight`, `credit`, `maxbuy`, `usermaxbuy`, `hasoption`, `dispatch`, `thumb_url`, `isnew`, `ishot`, `isdiscount`, `isrecommand`, `issendfree`, `istime`, `iscomment`, `timestart`, `timeend`, `viewcount`, `deleted`, `hascommission`, `commission1_rate`, `commission1_pay`, `commission2_rate`, `commission2_pay`, `commission3_rate`, `commission3_pay`, `score`, `taobaoid`, `taotaoid`, `taobaourl`, `updatetime`, `share_title`, `share_icon`, `cash`, `commission_thumb`, `isnodiscount`, `showlevels`, `buylevels`, `showgroups`, `buygroups`, `isverify`, `storeids`, `noticeopenid`, `tcate`, `noticetype`, `needfollow`, `followtip`, `followurl`, `deduct`, `virtual`, `ccates`, `discounts`, `nocommission`, `hidecommission`, `pcates`, `tcates`, `cates`, `artid`, `detail_logo`, `detail_shopname`, `detail_btntext1`, `detail_btnurl1`, `detail_btntext2`, `detail_btnurl2`, `detail_totaltitle`, `saleupdate42392`, `deduct2`, `ednum`, `saleupdate`, `edmoney`, `edareas`, `diyformtype`, `diyformid`, `diymode`, `dispatchtype`, `dispatchid`, `dispatchprice`, `manydeduct`, `shorttitle`, `isdiscount_title`, `isdiscount_time`, `isdiscount_discounts`, `commission`, `saleupdate37975`, `shopid`, `allcates`, `minbuy`, `invoice`, `repair`, `seven`, `money`, `minprice`, `maxprice`, `province`, `city`, `buyshow`, `buycontent`, `saleupdate51117`, `virtualsend`, `virtualsendcontent`, `verifytype`, `diyfields`, `diysaveid`, `diysave`, `quality`, `groupstype`, `showtotal`, `subtitle`, `minpriceupdated`, `newgoods`, `video`, `officthumb`, `sharebtn`, `catesinit3`, `showtotaladd`, `merchid`, `checked`, `thumb_first`, `merchsale`, `keywords`, `catch_id`, `catch_url`, `catch_source`, `saleupdate40170`, `saleupdate35843`, `labelname`, `autoreceive`, `cannotrefund`, `saleupdate33219`, `bargain`, `buyagain`, `buyagain_islong`, `buyagain_condition`, `buyagain_sale`, `buyagain_commission`, `saleupdate32484`, `saleupdate36586`, `diypage`, `cashier`, `saleupdate53481`, `saleupdate30424`, `isendtime`, `usetime`, `endtime`, `merchdisplayorder`, `exchange_stock`, `exchange_postage`, `ispresell`, `presellprice`, `presellover`, `presellovertime`, `presellstart`, `preselltimestart`, `presellend`, `preselltimeend`, `presellsendtype`, `presellsendstatrttime`, `presellsendtime`, `edareas_code`, `unite_total`, `buyagain_price`, `threen`, `intervalfloor`, `intervalprice`, `isfullback`, `isstatustime`, `statustimestart`, `statustimeend`, `nosearch`, `showsales`, `islive`, `liveprice`, `opencard`, `cardid`, `verifygoodsnum`, `verifygoodsdays`, `verifygoodslimittype`, `verifygoodslimitdate`, `minliveprice`, `maxliveprice`, `dowpayment`, `tempid`, `isstoreprice`, `beforehours`, `verifygoodstype`, `isforceverifystore`, `manydeduct2`)
        values(7, '%d', 0, 1, 1, 0, '%s', '%s', '', '', '', '',
     '', '%s', '%s', '0.00', '0.00', '%d', 0, 0, 0, '', 1576254445, '0.00', '', 0, 0, 0, 0, 'a:0:{}', 0, 0,
     0, 0, 0, 0, 0, 1576254420, 1576859220, 0, 0, 0, '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '',
     '', '', 0, '', '', 0, '', 0, '', '', '', '', 1, '', '', 0, '', 0, '', '', '0.00', 0, '',
     '{"type":"0","default":"","default_pay":"","level16":"","level16_pay":"","level17":"","level17_pay":"","level18":"","level18_pay":"","level19":"","level19_pay":"","level20":"","level20_pay":""}',
     0, 0, '', '', '', 0, '', '', '', '', '', '', '', 0, '0.00', 0, 0, '0.00', '', 0, 0, 0, 0, 0, '0.00', 0, '',
     '', 1576254420,
     '{"type":0,"default":{"option0":""},"level16":{"option0":""},"level17":{"option0":""},"level18":{"option0":""},"level19":{"option0":""},"level20":{"option0":""}}',
     '{"type":0}',
     0, 0, NULL , 0, 0, 0, 0, '', '12.00', '12.00', '请选择省份', '请选择城市', 0, '', 0, 0, '', 0, NULL, 0, 0, 0, 0, 0,
     '', 0, 0, '', NULL , 0, NULL , 0, 0, 0, 0, 0, '', '', '', '', 0, 0, 'N;', 0, 0, 0, 0, '0.00', 0, 0, 0, NULL , 0,
     0, 0, 0, 0, 0, 0, 0, 1576254420, 0, 0, '0.00', 0, '0.00', 0, 0, 0, 0, 0, 0, 0, 1576254420, 0, '', 0, '0.00', '', 0,
     '', 0, 0, 1576254360, 1578932760, 0, 1, 0, '0.00', 0, '', 1, 1, 0, 0, '0.00', '0.00', '0.00', 0, 0, 0, 0, 0, 0)

    ''' % (product_type, product_name, product_image, product_price, product_cur_price, inventory)

    cursor.execute(sql)
    db.commit()


def get_pd_data():
    type_id_dic = {
        '主食蛋品': 1203,
        '可口蔬菜': 1201,
        '应季水果': 1197,
        '新鲜肉禽': 1198,
        '海鲜水产': 1199
    }

    db = pymysql.connect("localhost", "root", "", "mall_wzxmf_com")
    cursor = db.cursor()
    inventory = 1000
    count = 0
    product_file_list = os.listdir('./xlsx')
    for j in product_file_list:
        pd_data = pd.read_excel('./xlsx/' + j)
        for i in range(len(pd_data)):
            product_name = pd_data.iat[i, 1]
            product_image = pd_data.iat[i, 2]
            product_cur_price = pd_data.iat[i, 3]
            product_price = pd_data.iat[i, 4]
            product_type = type_id_dic[pd_data.iat[i, 5]]
            print((product_name, product_image, product_cur_price, product_price, product_type))
            connection_mysql(db, cursor, product_type, product_name, product_image, product_cur_price, product_price, inventory)
            db.commit()
            count += 1
    db.close()
    print(count)


def delete_duplicates():
    pd_list = os.listdir('./xlsx')
    for filename in pd_list:
        df = pd.read_excel('./xlsx/' + filename)
        first_pd = df.drop_duplicates(subset=['产品图片'], keep='first')
        new_f = pd.DataFrame([], columns=first_pd.columns.to_list())
        type_set = set()
        new_ls = []

        for i in first_pd['产品名称'].tolist():
            if i.split('约')[0] not in type_set:
                new_ls.append(i)
            type_set.add(i.split('约')[0])

        c = 0
        for i, v in enumerate(first_pd.index.to_list()):
            if first_pd.iat[c, 1] in new_ls:
                new_f = new_f.append(first_pd.iloc[i:i + 1, :], ignore_index=True)
            c += 1

        new_f.to_excel('./new_xlsx/' + filename.replace('_', '_new_'), index=False)


