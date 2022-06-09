import requests

url = "https://www.goatbots.com/trending/pauper"

payload = ""
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    'Accept-Language': "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
    'Accept-Encoding': "gzip, deflate, br",
    'DNT': "1",
    'Connection': "keep-alive",
    'Cookie': "PHPSESSID=0rv4sl01ln9o5aht832d5hmfl1; __cf_bm=azDa5itxVT.5mypEHDzgaiWzPsl3RfgXhJPbcevx7.Q-1652472496-0-AQagBQaVDKFVouPclW04VYFu5LjyyBVBbt/ttSzCyAIUabB/cAa0Vk50HFD3UjW0I31jQOAo6qIQErnG9Dypqhcfelveva1KydYCLzmoZiEm9j4NRW8dKR0E4jNW4fb3KZsoF3ESm2s7yfTVYqi+pKgt4AZxljTOtH0oAcV7QQb1",
    'Upgrade-Insecure-Requests': "1",
    'Sec-Fetch-Dest': "document",
    'Sec-Fetch-Mode': "navigate",
    'Sec-Fetch-Site': "none",
    'Sec-Fetch-User': "?1",
    'TE': "trailers",
    'Content-Type': "application/x-www-form-urlencoded"
    }

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)