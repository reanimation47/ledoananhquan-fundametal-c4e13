from urllib.request import urlopen
from bs4 import BeautifulSoup

#1. Download webpage
url = 'http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn'
website = urlopen(url)
html_content = website.read().decode('utf8')

#2. Put html_content into soup
soup = BeautifulSoup(html_content,'html.parser')

#3.Find
table_data= soup.find('table', id= 'tableContent')
#
# temp = open('temp.html','w')
# temp.write(table_data.prettify())
# temp.close()

trs = table_data.find_all('tr')

data_list =[]


for tr in trs:

    tds = tr.find_all('td')
    data = {}

    for index, td in enumerate(tds):
        content = td.string

        if content != None:
            if index == 0:
                data['title'] = content.strip()
            elif index ==1:
                data['Quý 4- 2016'] = content
            elif index == 2:
                data['Quý 1- 2017'] = content
            elif index == 3:
                data['Quý 2 - 2017']= content
            elif index ==4:
                data['Quý 3- 2017'] = content

    if data != {}:
        data_list.append(data)
print(data_list)
