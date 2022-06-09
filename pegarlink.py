import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

url = 'https://www.ligamagic.com.br/?view=cards/search&card=ed%3Dclb'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

#script = soup.find('script').text.strip()[58:-1]

#data = json.loads(script)

links = []
for link in soup.find_all('a'):
    full_url = urljoin(url, link['href']) # join domain to path
    links.append(full_url)

print(links)