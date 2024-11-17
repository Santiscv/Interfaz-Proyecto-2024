import requests
from bs4 import BeautifulSoup

def obtener_lista_guitarras(urlPagina):
    try:
        response = requests.get(urlPagina, timeout=10)  #establece un timeout de 10 segundos
        soup = BeautifulSoup(response.text, "lxml")

        # seleccionamos los elementos <a> para obtener los nombres y rutas
        price = soup.select(".mt-0 .pecio_final b")
        titles = soup.select(".card-title a")

        guitars_list = []

        # recorremos cada elemento para extraer el nombre y la ruta
        for title in titles:
            href = title['href']
            part = href.split('/guitarras-electroacusticas/')[-1]
            name = title.text.strip()  # Obtenemos el nombre de la guitarra
            guitars_list.append({"nombre": name, "ruta": part})

            # recorremos los precios y los añadimos al diccionario correspondiente
        for i, price in enumerate(price):
            price_text = price.get_text(strip=True).replace("$", "").replace(",", "")
            price_float = float(price_text)
            if i < len(guitars_list):
                guitars_list[i]["precio"] = price_float

            # añadimos detalles adicionales para cada guitarra
        for guitarra in guitars_list:
            print(f"Obteniendo detalles para: {guitarra['nombre']}")
            detalles = obtener_detalles_guitarra(guitarra["ruta"])
            guitarra.update(detalles)

        return guitars_list

    except requests.exceptions.Timeout:
        print("La solicitud ha tardado demasiado y ha sido cancelada.")
        return []

def obtener_detalles_guitarra(ruta):
    try:
        url_detalle = f"https://www.casalibertella.com/instrumentos-de-cuerdas/guitarras-electroacusticas/{ruta}"
        response = requests.get(url_detalle, timeout=10)  # Establece un timeout de 10 segundos
        soup = BeautifulSoup(response.text, "lxml")

        origin = soup.select(".card-body")

            # diccionario para almacenar los resultados
        details = {
            "Origen": "no encontrado",
            "Trastera": "no encontrado",
            "Micrófonos": "no encontrado"
        }

            # recorremos cada elemento para buscar los textos
        for card in origin:
            text = card.get_text(separator="\n").split("\n")
            for line in text:
                if "Origen:" in line and details["Origen"] == "no encontrado":
                    details["Origen"] = line.replace("Origen:", "").strip()
                elif "Trastera:" in line and details["Trastera"] == "no encontrado":
                    details["Trastera"] = line.replace("Trastera:", "").strip()
                elif "Micrófonos:" in line and details["Micrófonos"] == "no encontrado":
                    details["Micrófonos"] = line.replace("Micrófonos:", "").strip()

        return details

    except requests.exceptions.Timeout:
        print(f"La solicitud para {ruta} ha tardado demasiado y ha sido cancelada.")
        return {
            "Origen": "no encontrado",
            "Trastera": "no encontrado",
            "Micrófonos": "no encontrado"
        }


        