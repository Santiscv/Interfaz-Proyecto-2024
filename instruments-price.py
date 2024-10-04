
import requests
from bs4 import BeautifulSoup

# Define the URL
urlPagina = "https://www.casalibertella.com/instrumentos-de-cuerdas/guitarras-electroacusticas/"
response = requests.get(urlPagina)


soup = BeautifulSoup(response.text, "lxml")

price= soup.select(".mt-0 .pecio_final b" )
title= soup.select(".card-title a")

for routes in title:
    href = routes['href']
    part = href.split('/guitarras-electroacusticas/')[-1]
    print(part)

title_list=[]

for title in title:
     title_guitar= title.text
     title_list.append(title_guitar)
# print(title_list)

price_list = []

for price in price:
     price_text = price.get_text(strip=True)  
     price_list.append(price_text)


