import requests
from bs4 import BeautifulSoup as soup


search = "iphone 11"
url = f'https://www.olx.com.eg/en/mobile-phones-tablets-accessories-numbers/mobile-phones/q-{search}/'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
s = requests.Session()
s.headers.update(headers)

r = s.get(url)

cont = soup(r.content,  "lxml")

ads = cont.findAll('div',{'class':'ads__item'})

for item in ads:
    tag = item.find('div',{'class':'ads__item__info'})
    print('#########')
    print(type(tag))
    print('----------------------------------------')

print(len(ads))