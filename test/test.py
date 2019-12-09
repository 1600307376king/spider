import requests
from bs4 import BeautifulSoup
import random


def get_html():
    url = 'https://www.xicidaili.com/nn/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',

    }
    html_text = ''
    response_text = requests.get(url, headers=headers)
    if response_text.status_code == 200:
        html_text = response_text.text

    return html_text


def get_proxy_data(text):
    soup = BeautifulSoup(text, 'lxml')
    all_msg_list = soup.find_all('tr')
    ip_list = []
    for i in all_msg_list:
        tmp = i.find_all('td')
        ip_list.extend(tmp[1] if len(tmp) > 0 else [])
    return ip_list, len(ip_list)


print(get_proxy_data(get_html()))
