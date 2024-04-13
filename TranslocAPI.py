import requests
import pandas as pd





stopsurl = "https://transloc-api-1-2.p.rapidapi.com/stops.json"

querystring = {"agencies":"603","callback":"call"}

headers = {
	"X-RapidAPI-Key": "7f4b672159msh144c69cf18b59eep15426bjsn54f9e4caec64",
	"X-RapidAPI-Host": "transloc-api-1-2.p.rapidapi.com"
}

response = requests.get(stopsurl, headers=headers, params=querystring)

print(response.json())

df = pd.DataFrame.from_dict(response.json()['data'])
print(df)