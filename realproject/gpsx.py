import requests
import json
from decimal import *


user_gps= 'http://freegeoip.net/json'
r = requests.get(user_gps)
js = json.loads(r.text)
lat = js['latitude']
lon = js['longitude']
getcontext().prec = 20

print(Decimal(lat),Decimal(lon))
