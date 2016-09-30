import urlib2
import json
request = Request('http://api.sunrise-sunset.org/json?lat=51.4386470&lng=-0.3189160')
responce = urlopen(request)
sunset = responce.read()
sunsetdict = json.loads(sunset)


print(sunsetdict['sunset'])


