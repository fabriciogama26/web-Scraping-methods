from requests_html import HTMLSession

listeds=[]

with open("cards.txt") as file:
    for x in file:

        url = "https://www.goatbots.com/card/"f"{x}"

        s = HTMLSession()

        r = s.get(url)

        r.html.render(sleep=1, timeout=20)

        price = r.html.css('div.dygraph-legend', first = True).text
        #//*[@id="graph-legend"]
        #.dygraph-legend

        listeds.append({"Preço":[price]})


print(listeds)