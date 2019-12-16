#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/14 0014 10:40
# @Author  : HelloWorld
# @File    : insert_data.py

import pymysql
import os
import pandas as pd
import numpy as np


def connection_mysql(db, cursor, product_type, product_name, product_image, product_price, product_cur_price, inventory):
    # productprice 原价 marketprice 市场价
    #
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

    ''' % (product_type, product_name, 'images/7/2019/09/' + product_image.split('/')[-1], product_price, product_cur_price, inventory)

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
    product_file_list = os.listdir('./new_xlsx')
    for j in product_file_list:
        pd_data = pd.read_excel('./new_xlsx/' + j)
        for i in range(len(pd_data)):
            product_name = pd_data.iat[i, 1]
            product_image = pd_data.iat[i, 2]
            product_cur_price = pd_data.iat[i, 3]
            product_price = pd_data.iat[i, 4]
            product_type = type_id_dic[pd_data.iat[i, 5]]
            print((product_name, product_image, product_cur_price, product_price, product_type))
            connection_mysql(db, cursor, product_type, product_name, product_image, product_price, product_cur_price, inventory)
            db.commit()
            count += 1
    db.close()
    print(count)




a = """
1526
7
1197
0
1
1
0
哈密瓜约2.0kg/份
images/7/2019/09/58a3b2e0N4a5cae75.jpg
0.00
35.00
0.00
0.00
1000
0
0
0
1576254445
0.00
0
0
0
0
a:0:{}
0
0
0
0
0
0
0
1576254420
1576859220
0
0
0
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0
0
0
1
0
0
0.00
0
{"type":"0","default":"","default_pay":"","level16...
0
0
0
0
0.00
0
0
0.00
0
0
0
0
0
0.00
0
1576254420
{"type":0,"default":{"option0":""},"level16":{"opt...
{"type":0}
0
0
NULL
0
0
0
0
35.00
35.00
请选择省份
请选择城市
0
0
0
0
NULL
0
0
0
0
0
0
0
NULL
0
NULL
0
0
0
0
0
0
0
N;
0
0
0
0
0.00
0
0
0
NULL
0
0
0
0
0
0
0
0
1576254420
0
0
0.00
0
0.00
0
0
0
0
0
0
0
1576254420
0
0
0.00
0
0
0
1576254360
1578932760
0
1
0
0.00
0
1
1
0
0
0.00
0.00
0.00
0
0
0
0
0
0

"""
b = """
1526
7
1197
0
1
1
0
哈密瓜约2.0kg/份
images/7/2019/09/58a3b2e0N4a5cae75.jpg
0.00
35.00
0.00
0.00
1000
0
0
0
1576254445
0.00
0
0
0
0
a:0:{}
0
0
0
0
0
0
0
1576254420
1576859220
0
0
0
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0
0
0
1
0
0
0.00
0
{"type":"0","default":"","default_pay":"","level16...
0
0
1197
1197
0
0
0.00
0
0
0.00
0
0
0
0
0
0.00
0
1576254420
{"type":0,"default":{"option0":""},"level16":{"opt...
{"type":0}
0
0
NULL
0
0
0
0
35.00
35.00
请选择省份
请选择城市
0
0
0
0
NULL
0
0
0
0
0
0
0
NULL
0
NULL
0
0
0
0
0
0
0
N;
0
0
0
0
0.00
0
0
0
NULL
0
0
0
0
0
0
0
0
1576254420
0
0
0.00
0
0.00
0
0
0
0
0
0
0
1576254420
0
0
0.00
0
0
0
1576254360
1578932760
0
1
0
0.00
0
1
1
0
0
0.00
0.00
0.00
0
0
0
0
0
0
"""
# for i, v in enumerate(a.split('\n')):
#     if b.split('\n')[i] != v:
#         print(i)
#         print('b=' + b.split('\n')[i] + '----' + 'a=' + v)
# arr = np.array()
# df = pd.DataFrame(arr)
# print(arr.shape)


