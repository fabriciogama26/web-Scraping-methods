import requests
import pandas as pd

url = "https://www.ligamagic.com.br/"

res=[]

querystring = {"id":"GTM-TW6DML","view":"cards/search","card":"edid=479911 ed=clb"}

payload = ""
headers = {
    'cookie': "PHPSESSID=a95358a8d6a76db9884bf8e5745ba0f0",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0",
    'Accept': "*/*",
    'Accept-Language': "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
    'Accept-Encoding': "gzip, deflate, br",
    'Alt-Used': "www.googletagmanager.com",
    'Connection': "keep-alive",
    'Referer': "https://www.ligamagic.com.br/",
    'Sec-Fetch-Dest': "script",
    'Sec-Fetch-Mode': "no-cors",
    'Sec-Fetch-Site': "cross-site",
    'If-Modified-Since': "Sat, 28 May 2022 12:00:00 GMT"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

data = response.text

for i in data:
    res.append(i)
        

df = pd.json_normalize(res)
df.to_csv("liga.csv")