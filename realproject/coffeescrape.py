from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://www.foody.vn/ha-noi/cafe?c=cafe")
html_content = html.read().decode('utf-8')
html.close()

soup = BeautifulSoup(html_content,'html.parser')
cf = soup.find_all("div", {"class": "resname"})

img = soup.find_all("div", {"class": "ri-avatar result-image"})

for cafename in cf:

    link = cafename.find("a",href=True)


    content = cafename.text

    if "chi nhánh" in content:
        inlink = link['href']

        chinhanh = urlopen('https://www.foody.vn{0}'.format(inlink))
        incontent = chinhanh.read().decode('utf-8')
        chinhanh.close()
        soups = BeautifulSoup(incontent,'html.parser')
        cfs = soups.find_all("div", {"class": "ldc-item-h-name"})
        for x in cfs :

            contents = x.text

            print(contents)
            print("---------------------------")
    else:
            print(content)
            print("-"*20)
