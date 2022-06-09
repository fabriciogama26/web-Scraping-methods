from requests_html import HTMLSession
import pandas as pd

url = "https://www.ligamagic.com.br/?view=cards/search&card=ed%3Dclb"
s = HTMLSession()

r = s.get(url)

r.html.render(timeout=20)

cards = r.html.xpath("/html/body/main/div[3]/div[3]/div[3]/div", first=True)

listcards = []

for item in cards.absolute_links:
    r = s.get(item)
    
    try:
        nome = r.html.find('p.nome-auxiliar', first=True).text
        price = r.html.find('div.col-prc col-prc-menor', first=True).text
        listcards.append({"Nome":[nome], "Valor":[price]})

    except:
        nome = "none"
        price = "none"
        
df = pd.DataFrame(listcards)

df.to_csv("liga.csv")




   
  
    