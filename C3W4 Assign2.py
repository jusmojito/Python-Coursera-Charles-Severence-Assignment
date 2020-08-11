import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
html=urllib.request.urlopen('http://py4e-data.dr-chuck.net/known_by_Fikret.html')
l=list()
visiturl=None
anchortag=None
soup=BeautifulSoup(html,"html.parser")

'''tags=soup('a')
for tag in tags:
    #print(tag)
    name=re.findall("_by_([a-zA-Z]+).+",str(tag))
    for n in name:
        l.append(n)
print(l)
print(tags[4])
#print(type(tags))
'''
#n=int(input())
#p=int(input())
for t in range(0,5):
    if visiturl is None:
        visiturl='http://py4e-data.dr-chuck.net/known_by_Fikret.html'
    else:
        anchortag=tags[2]
        #print(anchortag)
        visiturl=anchortag['href']
        print(visiturl)
    html=urllib.request.urlopen(visiturl)
    soup=BeautifulSoup(html,"html.parser")
    tags=soup('a')
    

#print(visiturl)
name=re.findall("_by_([a-zA-Z]+).+",visiturl)
print(name[0])

    
