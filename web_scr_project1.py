import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
cc=0
url=input('Enter URL: ')
cnnt=input('Enter count: ')
pos=input('Enter position: ')
print(url)
while cc<int(cnnt):
    html=urllib.request.urlopen(url, context=ctx).read()
    soup=BeautifulSoup(html, 'html.parser')
    tags=soup('a')
    lst=list()
    for tag in tags:
        lst.append(tag.get("href", None))
    url=lst[int(pos)-1]
    cc+=1
    print(url)
