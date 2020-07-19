import requests

url = "https://api.daily.co/v1/"

headers = {'authorization': 'Bearer 126d5b4f5620fdea318f72c06e895f9a4cf90948177ff40fa73cf824d8128d24'}

response = requests.request("GET", url, headers=headers)

print(response.text)