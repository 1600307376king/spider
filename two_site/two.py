# coding=utf8
import requests
from bs4 import BeautifulSoup
import time
from lxml import etree
import pymysql


# 卜易居
def get_html(a, b):
    url = 'https://www.buyiju.com/peidui/xzpd.php'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/74.0.3729.131 Safari/537.36'
    }
    data = {
        'xz1': a,
        'xz2': b,
        'submit': '开始测试'
    }

    res = requests.post(url, data=data, headers=headers)

    if res.status_code == 200:
        return res.text

    return '爬取异常'


def analytical(html):
    soup = BeautifulSoup(html, 'lxml')
    data = soup.find(class_='content')
    h = etree.HTML(str(data))
    obj = h.xpath('//p/font/text()')[0]
    score = h.xpath('//p/text()')[1]
    res = h.xpath('//p/text()')[2]
    return obj, score, res


def save_data(data):
    db = pymysql.connect('localhost', 'root', '123456', 'constellation')
    cursor = db.cursor()
    sql = """insert into buyiju(obj, score, res) values ('{}', '{}', '{}')
    """.format(data[0], data[1], data[2])
    print(sql)
    cursor.execute(sql)
    db.commit()

    db.close()
s = '''
<div class="content">
<p>您测试的星座配对结果如下：</p>
<p><font color="#ff0000">白羊座 VS 白羊座</font></p>
<p><b>星座配对指数：</b></p>
<p>友情：★★★★★
爱情：★★★★
婚姻：★★★
亲情：★★★★</p>
<p><b>星座爱情配对：</b></p>
<p>两个一模一样的白羊座在一起，必然是爆炸性的组合。
两人会很快被对方相同的行为态度吸引在一起。他们不会转弯抹角，而是直接表达出自己的爱意，马上进入热恋的阶段。不过他们过于相同的思想行为，相处久后会逐渐无法容忍对方的缺点，加上自私和不服输的性格，在没完没了的争吵中，对对方的爱意会变成讨厌甚至仇恨。另外，一旦两个人成为夫妻，一定要在理财计划上好好处理，否则入不敷出。 
性生活方面，充满活力的两人配合度相当高。只是太着重性生活而忽略心灵上的沟通也是他们之间的大问题。</p>
<p></p><div class="yunshi"><a href="http://ds.buyiju.com/vip/hh/?from=xzpd">八字合婚精批： 天生一对还是欢喜冤家？</a></div>
</div>
'''
# h = etree.HTML(s)
# obj = h.xpath('//p/font/text()')[0]
# score = h.xpath('//p/text()')[1]
# res = h.xpath('//p/text()')[2]
# print(score)
co = ['白羊座', '金牛座',
      '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座', '水瓶座', '双鱼座']
for i in co:
    for k in co:
        save_data(analytical(get_html(i, k)))
        time.sleep(1)

