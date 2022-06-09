from requests_html import HTMLSession
import pandas as pd

res = []

url = "https://www.ligamagic.com.br/?view=cards/search&card=edid=479911%20ed=clb"

s = HTMLSession()

r = s.get(url)

data = r.json()

for i in data:
    res.append(i)

df = pd.json_normalize(res)

df.to_csv("liga.csv")