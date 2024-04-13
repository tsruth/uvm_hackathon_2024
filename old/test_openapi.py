import requests

url = "https://transloc-api-1-2.p.rapidapi.com/agencies.json"

querystring = {"callback":"call","geo_area":"35.80176,-78.64347|35.78061,-78.68218","agencies":"12"}

headers = {
	"X-RapidAPI-Key": "7607785db6msh4ee9c3264053a21p1ea8b5jsne39e6e6b06fb",
	"X-RapidAPI-Host": "transloc-api-1-2.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
