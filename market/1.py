import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.seoul.go.kr/economy/archives/category/nationaleconomy-news_c1/tradition_make_c1/traditioninfo_biz_nationaleconomy-n1')
soup = BeautifulSoup(res.content, 'html.parser')

post_list = []

for links in soup.select('div.post-lst div.child_policyDL_R'):

    title = links.select('h3.tit a')
    link = links.select('h3.tit a')
    made_time = links.select('span.time')

    title = title[0].get('title')
    link = link[0].get('href')
    made_time = made_time[0].get_text()[0:19]

    post = {'title' : title,
            'link' : link,
            'made_time' : made_time
            }

    post_list.append(post)


