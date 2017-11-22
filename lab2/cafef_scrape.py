from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn")
html_content = html.read().decode('utf-8')
html.close()

soup = BeautifulSoup(html_content,'html.parser')
tr_news = soup.find('table', id ='tableContent')

tr_news_list = tr_news.find_all('tr')

for tr in tr_news_list:
    a = tr.td
    details =  a['title']
    content = a.string
    print(content)
    print("-"*20)
