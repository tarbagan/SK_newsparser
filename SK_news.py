import requests
from bs4 import BeautifulSoup as bs
import re

def get_url():
    page = set()
    poisk = u"женщина"
    url = u"http://tuva.sledcom.ru/search/?q="+poisk+"&page="
    for i in range(1,23):
        page.add(url+str(i))
    return page

def get_content():
    for get in get_url():
        r = requests.get(get,timeout=1)
        soup = bs(r.text, 'lxml')
        for t in soup.findAll('div',{'class':'bl-item-title'}):
            tit = (t.text)
            tit = re.sub(r'[\ \n]{2,}', '', tit)
            print (tit) 
