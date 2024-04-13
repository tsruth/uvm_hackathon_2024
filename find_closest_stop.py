import certifi
import ssl
import geopy.geocoders
from geopy.geocoders import Nominatim
import math

def find_distances(stop1, stop2):
    ctx = ssl.create_default_context(cafile=certifi.where())
    geopy.geocoders.options.default_ssl_context = ctx
    nom = Nominatim(scheme = 'http', user_agent="Test")
    dictOfPlacesToCords = {'Downtown Transit Center – A, C, E, G, I': 'Downtown Transit Center, Burlington',
                       'Downtown Transit Center': 'Downtown Transit Center, Burlington',
                       'Downtown TransitCenter – B, D, F, H, J' : 'Downtown Transit Center, Burlington',
                       'University Heights': 'University Heights, Burlington',
                       'University Mall': '155 Dorset St, South Burlington',
                       'Williston Road at Kennedy Drive': '1800 Williston Rd, South Burlington',
                       'White Cap Business Park': '426 Industrial Ave, Williston',
                       'Walmart': '863 Harvest Ln, Williston',
                       'UVM Medical Center': 'University of Vermont Medical Center, 111 Colchester Ave, Burlington, VT 05401',
                       'Winooski Falls at Champlain Mill': '25 Winooski Falls Way, Winooski, VT 05404',
                       'Saint Michael’s College': 'Saint Michael’s College',
                       'Fort Ethan Allen at Catamount Lane': "223 Ethan Allen Ave, Colchester, VT 05446",
                       'Global Foundries': '1490 Robinson Pkwy, Essex Junction, VT 05452',
                       'Amtrak Station': '29 Railroad Ave, Essex Junction, VT 05452',
                       'Spinner Place at Champlain Mill': '25 Winooski Falls Way, Winooski, VT 05404',
                       '230 Saint Paul Street': '230 Saint Paul Street, Burlington',
                       'Howard Center': '1138 Pine St, Burlington, VT 05401',
                       'Green Mountain Transit Administrative Office': '101 Queen City Park Rd, Burlington, VT 05401',
                       'Shelburne Road at Home Avenue':'229 Home Ave, Burlington, VT 05401',
                       'Shelburne Road at Allen Road': '1820 Shelburne Rd, South Burlington, VT 05403',
                       'Shelburne Museum': '6000 Shelburne Rd, Shelburne, VT 05482',
                       'Vermont Teddy Bear Factory': '6655 Shelburne Rd, Shelburne, VT 05482',
                       'Downtown BHS': '67 Cherry St, Burlington, VT 05401',
                       'Burlington High School':'52 Institute Rd, Burlington, VT 05408',
                       'Ethan Allen Shopping Center': '1199 North Ave, Burlington, VT 05408',
                       'Heineberg Housing': '14 Heineberg Rd, Burlington, VT 05408',
                       'Northgate Road': '1907 North Ave, Burlington, VT 05408',
                       'North Street at N Union Street': '144 N Union St, Burlington, VT 05401',
                       'Fern Hill': '214 N Prospect St #1, Burlington, VT 05401',
                       'McAuley Square': '130 Mansfield Ave UNIT 307, Burlington, VT 05401',
                       'UVM Waterman Building': '85 S Prospect St, Burlington, VT 05401',
                       'Maple Street at S Willard Street': '232 S Willard St, Burlington, VT 05401',
                       'Battery Street at College Street': '125 Battery St, Burlington, VT 05401',
                       'Courtyard': '25 Cherry St, Burlington, VT 05401',
                       '83 Barlow Street': '83 Barlow Street, Winooski',
                       'Weaver Street at Tigan Street':'1 Tigan St Suite 103, Winooski, VT 05404',
                       'Hickok Street at Elm Street': '133 Hickok St, Winooski, VT 05404',
                       'Essex Experience': '21 Essex Way, Essex, VT 05452',
                       'Essex Center': '125 Center Rd, Essex Junction, VT 05452',
                       'Sand Hill Road at River Road':'240 River Rd, Essex Junction, VT 05452',
                       'Waterfront': '1 College St, Burlington, VT 05401',
                       'UHC Main Lobby':'1 S Prospect St # 6, Burlington, VT 05401',
                       'Kennedy Drive at Timber Lane': '36 Timber Ln, South Burlington, VT 05403',
                       'Country Park': '631 Hinesburg Rd, South Burlington, VT 05403',
                       'Burlington International Airport': '1200 Airport Dr, South Burlington, VT 05403',
                       'Davis Center': 'Dudley H. Davis Center, 590, Main Street, Burlington, Colchester, Chittenden County, Vermont, 05401, United States'}
    if stop1 in dictOfPlacesToCords:
        stop1 = dictOfPlacesToCords[stop1]
        result1 = nom.geocode(stop1)
    else:
        result1 = nom.reverse(stop1)
    if stop2 in dictOfPlacesToCords:
        stop2 = dictOfPlacesToCords[stop2]
        result2 = nom.geocode(stop2)
    else: 
        result2 = nom.reverse(stop2)
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

print(find_distances('Davis Center', 'Waterfront'))