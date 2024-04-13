# import requests
#
#
# querystring = {"agencies":"603", "callback":"call"}
# headers = {
#     "X-RapidAPI-Key": "7607785db6msh4ee9c3264053a21p1ea8b5jsne39e6e6b06fb",
#     "X-RapidAPI-Host": "transloc-api-1-2.p.rapidapi.com"
# }
#
#
# def fetch_routes():
#     url = "https://transloc-api-1-2.p.rapidapi.com/routes.json"
#
#     response = requests.get(url, headers=headers, params=querystring)
#
#     print(response.json())
#
#     # TODO: decode json into dataframe
#     # TODO: filter dataframe
