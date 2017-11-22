from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://dantri.com.vn/")
html_content = html.read().decode('utf-8')
html.close()



soup = BeautifulSoup(html_content,'html.parser')
ul_news = soup.find('ul', 'ul1 ulnew')
li_news_list = ul_news.find_all('li')

for li in li_news_list:
    a_detail = li.h4.a
    title= a_detail['title']
    content = a_detail.string
    print(content)
    print('-'* 20)
