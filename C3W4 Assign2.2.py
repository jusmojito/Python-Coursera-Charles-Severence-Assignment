import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
visiturl=None

for t in range(0,8):
    if visiturl is None:
        visiturl='http://py4e-data.dr-chuck.net/known_by_Belle.html'
    else:
        anchortag=tags[17]
        visiturl=anchortag['href']
        print(visiturl)
    html=urllib.request.urlopen(visiturl)
    soup=BeautifulSoup(html,"html.parser")
    tags=soup('a')
    

name=re.findall("_by_([a-zA-Z]+).+",visiturl)
print(name[0])

    
