import requests
import json

url = "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetLivenow"

querystring = {"timezoneOffset":"180","langId":"79","skinName":"sportaza","configId":"26","culture":"pt-br","countryCode":"BR","deviceType":"Desktop","numformat":"en","integration":"sportaza","sportId":"66","showAllEvents":"false","count":"10"}

payload = ""
headers = {
    'authority': "sb2frontend-altenar2.biahosted.com",
    'accept': "*/*",
    'accept-language': "pt-BR,pt;q=0.9",
    'origin': "https://sportaza.com",
    'referer': "https://sportaza.com/br/sport",
    'sec-ch-ua': "^\^"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

if response.status_code != 200: 
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

jsondata = json.loads(response.text)