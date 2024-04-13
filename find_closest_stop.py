import certifi
import ssl
import geopy.geocoders
from geopy.geocoders import Nominatim
import math

def find_distances(stop1, stop2):
    ctx = ssl.create_default_context(cafile=certifi.where())
    geopy.geocoders.options.default_ssl_context = ctx
    nom = Nominatim(scheme = 'http', user_agent="Test")
    # result1 = nom.reverse('44.475939,-73.196490')
    # result2 = nom.reverse('44.473917,-73.203903')
    result1 = nom.geocode(stop1)
    result2 = nom.geocode(stop2)
    if result1 == None or result2 == None:
        print("Couldn't find location")
        return
    else:
        return getDistance(result1.latitude, result2.latitude, result1.longitude, result2.longitude)

def getDistance(latitude1, latitude2, longitude1, longitude2):
    latitude1 = math.radians(latitude1)
    latitude2 = math.radians(latitude2)
    longitude1 = math.radians(longitude1)
    longitude2 = math.radians(longitude2)
    a = (math.pow(math.sin(latitude2 - latitude1)/2, 2)) + math.cos(latitude1) * math.cos(latitude2) * math.pow(math.sin((longitude1 - longitude2)/2), 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = 6371 * c
    distance = distance * 0.621371
    return distance

print(find_distances('Dudley H. Davis Center, 590, Main Street, Burlington, Colchester, Chittenden County, Vermont, 05401, United States', 'University Heights, Burlington'))