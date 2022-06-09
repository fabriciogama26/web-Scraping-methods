from requests_html import HTMLSession
import pandas as pd


url_principal = "https://www.ligamagic.com.br/?view=cards/home"
s = HTMLSession()

r = s.get(url_principal)

r.html.render(sleep=1)

ed = r.html.xpath("/html/body/main/div[2]/div/div[2]/div/table/tbody", first=True)

listlink=[]

for itens in ed.absolute_links:
    listlink.append({"Link": [itens]})


df = pd.DataFrame(listlink)


df.to_csv("link.csv")