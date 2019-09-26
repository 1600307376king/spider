# coding=utf8
import requests
from bs4 import BeautifulSoup
from lxml import etree
import pymysql
import time


# 第一星座网
def get_html(a, b):
    url = 'https://www.d1xz.net/astro/peidui/' + str(a) + '-' + str(b) + '.aspx'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/74.0.3729.131 Safari/537.36'
    }

    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        return res.text

    return '爬取异常'


def analytical(html):
    soup = BeautifulSoup(html, 'lxml')
    data = soup.find(class_='mfsm_wrap')

    h = etree.HTML(str(data))
    obj = h.xpath('//h1/text()')
    score = 0
    for k in h.xpath('//p//img/@src'):
        if k[-18:-14] == 'full':
            score += 1
        elif k[-18:-14] == 'half':
            score += 0.5
        else:
            score += 0
    pair = h.xpath('//p/text()')
    love = pair[4]
    family = pair[5]
    friendly = pair[6]
    note = pair[7]
    return obj[0], str(score), love, family, friendly, note


def save_data(data):
    db = pymysql.connect('localhost', 'root', '123456', 'constellation')
    cursor = db.cursor()
    sql = """insert into first_constellation(obj, score, love, family, friendly, note) values ('{}', '{}', '{}', '{}', 
    '{}', '{}')
    """.format(data[0], data[1], data[2], data[3], data[4], data[5])
    print(sql)
    cursor.execute(sql)
    db.commit()

    db.close()


# r = analytical(get_html())

# c = '<p>白羊 (男)</p>'
s = '''<div class="mfsm_wrap"><h1>白羊男白羊女配对</h1><div class="mfsm_xzpd"><div class="mfsm_xzpd_item"><img 
src="/statics/d1xz/pc/apps/peidui/images/icon/1.png"/><p>白羊 (男)</p></div><div class="mfsm_xzpd_item"><img 
src="/statics/d1xz/pc/apps/peidui/images/icon_vs.png?v=33b73f4"/><p>配对</p></div><div class="mfsm_xzpd_item"><img 
src="/statics/d1xz/pc/apps/peidui/images/icon/1.png"/><p>白羊 (女)</p></div></div><p 
class="tit"><span>配对查询：</span>白羊男VS白羊女</p><p><span>配对指数：</span><img class="star" 
src="/statics/d1xz/pc/apps/peidui/images/star_full.png?v=5cc9279"/><img class="star" 
src="/statics/d1xz/pc/apps/peidui/images/star_full.png?v=5cc9279"/><img class="star" 
src="/statics/d1xz/pc/apps/peidui/images/star_full.png?v=5cc9279"/><img class="star" 
src="/statics/d1xz/pc/apps/peidui/images/star_full.png?v=5cc9279"/><img class="star" 
src="/statics/d1xz/pc/apps/peidui/images/star_full.png?v=5cc9279"/></p><p><b>爱情配对：</b><br 
/>爱情上白羊男跟白羊女是绝配的那一种，因为两个人思维都很活跃，性格都很活泼。当他们跟别人在一起的时候，对方总是很难跟上他们的节奏，他们的反应实在是太快了。但是当白羊男跟白羊女在一起的时候，两个人一个眼神意会，就会知道对方什么意思了。所以他们的相处非常的融洽，基本上不会有什么矛盾，彼此会非常的幸福恩爱。</p><p><b>亲情配对：</b><br/>亲情上白羊男跟白羊女也是非常的合拍的。不像其他家庭，一个人想要做什么事情，其他人会一直阻碍，或是完全不支持。白羊男跟白羊女在一起就一点这样的问题都没有，每次都是全力支持对方。因为他们太了解彼此了，对方想要做什么事的话，那是十头牛都拉不回来的。既然如此，为什么不给予提供一点支持，让对方可以毫无遗憾呢。</p><p><b>友情配对：</b><br/>友情上白羊男跟白羊女一直都是别人羡慕的那种好哥们，好姐们。虽然两个人关系很好，彼此走得很亲近，但是没有人怀疑过他们的关系，因为他们一直就都是坦坦荡荡的那种。开玩笑也都是当着大家的面，从不会让人尴尬的。所以朋友或许一开始还会怀疑他们是不是有暧昧，但是最后也会十分确定，这两个人就是真的好朋友而已。</p><p><b>配对建议和注意事项：</b><br/>白羊男跟白羊女的相处模式，基本上是不用给予太多的建议的。因为他们是那种都很敏感，也都很懂得为别人着想的人。所以每次气氛稍微不对劲的时候，彼此都会及时的收敛起来，然后想办法去补救气氛。如果非要给一点建议的话，那就是白羊男跟白羊女是属于人来疯的那种，所以有时候得稍微克制一下自己的热情才行。</p><p class="tips">以上结果由第一星座网提供，仅供参考！</p><div class="mw_select"><span>男生星座</span><div class="public_select J_select"><span></span><select id="sl1"><option value="1">白羊座</option><option value="2">金牛座</option><option value="3">双子座</option><option value="4">巨蟹座</option><option value="5">狮子座</option><option value="6">处女座</option><option value="7">天秤座</option><option value="8">天蝎座</option><option value="9">射手座</option><option value="10">摩羯座</option><option value="11">水瓶座</option><option value="12">双鱼座</option></select></div><span>女生星座</span><div class="public_select J_select"><span></span><select id="sl2"><option value="1">白羊座</option><option value="2">金牛座</option><option value="3">双子座</option><option value="4">巨蟹座</option><option value="5">狮子座</option><option value="6">处女座</option><option value="7">天秤座</option><option value="8">天蝎座</option><option value="9">射手座</option><option value="10">摩羯座</option><option value="11">水瓶座</option><option value="12">双鱼座</option></select></div><a href="javascript:;" onclick="window.location=\'/astro/peidui/\'+document.getElementById(\'sl1\').value+\'-\'+document.getElementById(\'sl2\').value+\'.aspx\'">星座配对</a><!--start ads:1108--><a href="https://cs.d1xz.net/xingzuopd/?spread=d1xzffsmxzpd01" style="background-color: #ec460a;" target="_blank">专业配对</a><!--ads:1108 end--></div></div>'] '''


# h = etree.HTML(s)
# obj = h.xpath('//h1/text()')
# score = 0
# for k in h.xpath('//p//img/@src'):
#     if k[-18:-14] == 'full':
#         score += 1
#     elif k[-18:-14] == 'half':
#         score += 0.5
#     else:
#         score += 0
#
# pair = h.xpath('//p/text()')
# love = pair[4]
# family = pair[5]
# friendly = pair[6]
# note = pair[7]
# print(score)
# #
# # save_data((obj[0], str(len(score)), love, family, friendly, note))

# for i in range(1, 13):
#     for k in range(1, 13):
#         save_data(analytical(get_html(i, k)))
#         time.sleep(1)
#         print('success' + str(i) + '-' + str(k))

