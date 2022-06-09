from requests_html import HTMLSession
import pandas as pd

url = "https://www.ligamagic.com.br/?view=cards/search&card=ed%3Dclb"
s = HTMLSession()

r = s.get(url)

r.html.render(sleep=1, timeout=20)

nome = r.html.find('span.invisible-label')
price = r.html.find('div.avgp-minprc')

Listcards = []

for i, ii, in zip(range(len(price)), range(len(nome))):
    y = nome[ii].text
    x = price[i].text
    Listcards.append({'Nome': [y], 'Valor': [x]})


df = pd.DataFrame(Listcards)

df.to_csv("liga.csv", encoding='utf-8-sig')

list = pd.read_csv("liga.csv")

df = pd.DataFrame(list)

df = df.join(df["Nome"].str.strip("'\"[]").str.split(r'\\n', expand=True))

df.rename(columns={0:"PT", 1:"EN"}, inplace=True)

df['Valor']=df['Valor'].apply(lambda x: x[2:-2])

df.drop(columns=["Nome"], inplace=True)

df.to_csv("liga.csv", encoding='utf-8-sig')
