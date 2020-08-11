import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

#address='http://py4e-data.dr-chuck.net/comments_109228.xml'
address='http://python-data.dr-chuck.net/comments_217218.xml'
uh=urllib.request.urlopen(address)
data=uh.read()
print(data.decode())
#print(datas)
#print(type(datas))

tree = ET.fromstring(data)
results = tree.findall('comments/comment/count')

sum=0
for count in results:
    sum=sum+int(count.text)
print(sum)
