import requests
from bs4 import BeautifulSoup


urlPagina = "https://www.casalibertella.com/instrumentos-de-cuerdas/guitarras-electroacusticas/guitarra-electroacustica-fonseca-50ec-nueva-garantia-73071.html"
response= requests.get(urlPagina)
soup= BeautifulSoup(response.text, "lxml")
price= soup.select(".web_p .precio" )
onlyPrice= price[0]
onlyPrice=onlyPrice.text
formattedPrice= onlyPrice[1:7] #sacamos el signo de $
formattedPrice= formattedPrice.replace("" , "") #pasarlo a string
actualPrice= float(formattedPrice)

myMoney= 100
if myMoney < actualPrice:
     print("no lo podes comprar")
else:
     print("lo podes comprar")
# raw_code= response.text
# soup= BeautifulSoup(raw_code, "html.parser")
# soup= BeautifulSoup(raw_code, "lxml")
# print(soup.h2.string)
# var1= soup.find_all(class_='img-fluid p-4 mh-100')
# for elementos in var1:
#     print(elementos.select('title'))






















# Encuentra todas las secciones que contienen información de guitarras
# guitarras = sopa.find_all("img", class_="img-fluid p-4 mh-100")

# print(guitarras)
# Recorre cada guitarra encontrada y extrae la información
# for guitarra in guitarras:
#     # Extraer el nombre de la guitarra
#     nombre = guitarra.find("a", class_="product-item-link").get_text().strip()
    
#     # Extraer el precio
#     precio = guitarra.find("span", class_="price").get_text().strip()
    
#     # Extraer la imagen (si existe)
#     imagen_tag = guitarra.find("img", class_="product-image-photo")
#     imagen = imagen_tag['src'] if imagen_tag else "Sin imagen disponible"
    
#     # Imprime la información extraída
#     print(f"Guitarra: {nombre}")
#     print(f"Precio: {precio}")
#     print(f"Imagen: {imagen}")
#     print("-" * 50)

# print("Extracción completada.")
