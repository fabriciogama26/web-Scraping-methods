import aiohttp
import asyncio
import time

start_time = time.time()
url = "https://www.ligamagic.com.br/?view=cards/search&card=edid=479911%20ed=clb"



async def main():

    async with aiohttp.ClientSession() as session:
        r = session.get(url)
        cards = session.html.xpath(url, first=True)

        for item in cards.absolute_links:
            r = session.get(item)
    
            try:
                async with session.get(r) as resp:
                    
                    nome = r.html.find('p.nome-auxiliar', first=True).text
                    price = r.html.find('div.col-prc col-prc-menor', first=True).text
                    print(nome, "|", price)
             

            except:
                nome = "none"
                price = "none"

asyncio.run(main())