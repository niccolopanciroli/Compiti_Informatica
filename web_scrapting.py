import requests
from bs4 import BeautifulSoup as bs
r = requests.get("https://www.oraesatta.info/it/data-di-oggi/")
data = r.text
soup = bs(data, "html.parser")
#print(soup.title.string)
tmp = soup.select('#content > div > div > div p:nth-child(6)')
tmp1 = soup.select("title")
print(tmp1)
print(tmp[0].get_text())