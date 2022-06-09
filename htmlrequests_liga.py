from lxml import html
import requests

url = "https://www.ligamagic.com.br/"

#list=["Dust to Dust", "Pyroblast"]
listeds=[]

with open("cards.txt") as file:
    for x in file:

        querystring = {"id":"GTM-TW6DML","view":"cards/card","card":f"{x}"}

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

        r = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        data = html.fromstring(r.content)

        price = data.xpath('/html/body/main/div[4]/div[1]/div/div[4]/div[5]/div[2]/div[1]/div[2]/text()')
        #ed_sigla = r.html.xpath('/html/body/main/div[2]/div/div[2]/div/table/tbody/tr[1]/td[2]').text
        listeds.append({"Preço":[price]})



print(listeds)