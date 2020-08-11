import urllib.request as ur, urllib.parse as up,urllib.error as ue
import json

serviceurl='http://py4e-data.dr-chuck.net/geojson?'

while True:
    address=input("Enter Location")
    if len(address)<1:
        break

    url=serviceurl+up.urlencode({'address':address})

    print('Retreiving',url)
    uh=ur.urlopen(url)
    data=uh.read().decode()
    print("Retrieved", len(data),'characters')

    try:
        js=json.loads(data)
    except:
        js=None

    if not js or 'status' not in js or js['status']!="OK":
        print("Invalid Data")
        print(data)
        continue

    #print(json.dumps(js,indent=3))

    place_id=js['results'][0]['place_id']
    print(place_id)
''' lat=js['results'][0]['geometry']['location']['lat']
    lng=js['results'][0]['geometry']['location']['lng']
    print('lat',lat,'lng',lng)
    location=js['results'][0]['formatted_address']
    print(location)
'''
