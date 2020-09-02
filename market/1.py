import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.seoul.go.kr/economy/archives/category/nationaleconomy-news_c1/tradition_make_c1/traditioninfo_biz_nationaleconomy-n1')
soup = BeautifulSoup(res.content, 'html.parser')

# queryset = get_object_or_404(Market, pk=kwargs['pk']) # 마켓에서 사진 가져옴


title_list = []
link_list = []
made_time_list = []
html_content_list = []

for links in soup.select('div.post-lst div.child_policyDL_R'):
    title = links.select('h3.tit a')
    link = links.select('h3.tit a')
    made_time = links.select('span.time')

    title = title[0].get('title')
    link = link[0].get('href')
    made_time = made_time[0].get_text()[0:11]

    html_content = [title, link, made_time]

    # title_list.append(title)
    # link_list.append(link)
    # made_time_list.append(made_time)
    html_content_list.append(html_content)

# post = {'title': title_list,
#         'link': link_list,
#         'made_time': made_time_list,
#         'html_content': html_content_list
#         }
post = {
        'html_content': html_content_list
        # 'market': queryset
        }


