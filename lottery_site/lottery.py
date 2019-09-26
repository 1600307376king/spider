import requests
from bs4 import BeautifulSoup
import time
from lxml import etree
import pandas as pd
import numpy as np


def get_html(start, end):
    url = 'https://datachart.500.com/ssq/history/newinc/history.php?start=' + str(start) + '&end=' + str(end)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/74.0.3729.131 Safari/537.36'
    }
    data = {
        ''
    }

    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        return res.text

    return 'error'


def analytical(html):
    if html != 'error':
        soup = BeautifulSoup(html, 'lxml')
        data = soup.find_all(class_='t_tr1')
        lot_df = []
        n = 0
        for k in data:
            m = etree.HTML(str(k))
            issue = m.xpath('//td/text()')
            issue.pop(8)
            lot_df.append(issue)
            n += 1
            if n % 1000 == 0:
                print(n)

        df = pd.DataFrame(lot_df, index=range(len(data)),
                          columns=['期号', '1', '2', '3', '4', '5', '6',
                                   '蓝球', '奖池奖金', '一等奖注数', '一等奖奖金(元)',
                                   '二等奖注数', '二等奖奖金', '总投注额(元)', '开奖日期'])

        df.to_excel('./lottery_data.xlsx')
        return df

    else:
        return 'xxx'


h = analytical(get_html(10000, 19113))
print(h)
