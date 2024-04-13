import requests
import pandas as pd





stopsurl = "https://transloc-api-1-2.p.rapidapi.com/stops.json"

routesurl = "https://transloc-api-1-2.p.rapidapi.com/routes.json"


querystring = {"agencies":"603","callback":"call"}

headers = {
	"X-RapidAPI-Key": "7f4b672159msh144c69cf18b59eep15426bjsn54f9e4caec64",
	"X-RapidAPI-Host": "transloc-api-1-2.p.rapidapi.com"
}

responseStops = requests.get(stopsurl, headers=headers, params=querystring)

dfStops = pd.DataFrame.from_dict(responseStops.json()['data'])

columns_to_keep = ['location','stop_id','routes','name']
columns_to_drop = set(dfStops.columns) - set(columns_to_keep)

"""
 Dataframe of all stops
 Columns: [
 location  -- format: {'lat': 44.467529, 'lng': -73.198875}
 stop id   -- unique int
 routes    -- list of routes on stop
 name      -- name of stop
 ]
"""
dfStops = dfStops.drop(columns=columns_to_drop)
print(dfStops)


responseRoutes = requests.get(routesurl, headers=headers, params=querystring)
dfRoutes = dfStops = pd.DataFrame.from_dict(responseRoutes.json()['data']['603'])


dfRoutes = dfRoutes.drop(0,axis=0)


pd.set_option('display.max_colwidth', None)
print(dfRoutes)


