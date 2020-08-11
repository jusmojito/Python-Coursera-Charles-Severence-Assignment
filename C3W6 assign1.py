import urllib.parse as up,urllib.request as ur
import json

#url='http://py4e-data.dr-chuck.net/comments_42.json'
url='http://py4e-data.dr-chuck.net/comments_109229.json'
n=0
sumc=0
uh=ur.urlopen(url)
urldata=uh.read().decode()

js=json.loads(urldata)
#print(urldata)

print(json.dumps(js,indent=3))
print(len(js['comments']))

while n<50:
    count=js['comments'][n]['count']
    sumc=sumc+int(count)
    n=n+1
print(sumc)
    
