import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.seoul.go.kr/economy/archives/category/nationaleconomy-news_c1/tradition_make_c1/traditioninfo_biz_nationaleconomy-n1')
soup = BeautifulSoup(res.content, 'html.parser')
title_data = soup.find_all('h3', class_='tit')

print(title_data)
