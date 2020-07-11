import requests as rq
url = "https://tech.163.com/"
r = rq.get(url,timeout = 30)
r.encoding='GBK'
print(r.text)

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text,'lxml')
newest_lists = soup.find('div',class_ = "newest-lists")
print("最新快讯")
for news in newest_lists.find_all('li',class_ = "list_item"):
    info = news.find('a')
    if info:
        title = info.get_text().strip()
        link = str(info.get('href'))
        print(f"标题：{title}")
        print(f"链接：{link}")
        
print("广告1")
for news in soup.find_all('div',class_ = "ntes-nav-select-pop"):
     info = news.find('a')
     if info:
         app = info.get_text().strip()
         link = str(info.get('href'))
         print(f"应用：{app}")
         print(f"链接：{link}")
 
print("头条快讯")
for news in soup.find_all('div',class_ = "banner_main"):
    info = news.find('a')
    if info:
        title = info.get_text().strip()
        link = str(info.get('href'))
        print(f"标题：{title}")
        print(f"链接：{link}")
       

