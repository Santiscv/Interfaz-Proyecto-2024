import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.casalibertella.com/instrumentos-de-cuerdas/guitarras-electroacusticas/"

def obtener_sopa(url):
    response = requests.get(url, timeout=10)
    return BeautifulSoup(response.text, "lxml")

def obtener_lista_guitarras():
    soup = obtener_sopa(BASE_URL)
    elementos_precio = soup.select(".mt-0 .pecio_final b")
    elementos_titulo = soup.select(".card-title a")

    lista_guitarras = []
    for i in range(len(elementos_titulo)):
        titulo = elementos_titulo[i].text.strip()
        ruta = elementos_titulo[i]['href'].split('/guitarras-electroacusticas/')[-1]
        precio_texto = elementos_precio[i].get_text(strip=True).replace("$", "").replace(",", "")
        precio = float(precio_texto)

        guitarra = {
            "nombre": titulo,
            "ruta": ruta,
            "precio": precio
        }
        lista_guitarras.append(guitarra)

    return lista_guitarras

def obtener_detalles_guitarra(ruta):
    soup = obtener_sopa(BASE_URL + ruta)
    detalles = {"Origen": "no encontrado", "Trastera": "no encontrado", "Micrófonos": "no encontrado"}

    cuerpo_texto = soup.select_one(".card-body").get_text(separator="\n")
    lineas_texto = cuerpo_texto.split("\n")
    for linea in lineas_texto:
        if "Origen:" in linea:
            detalles["Origen"] = linea.split(":", 1)[-1].strip()
        elif "Trastera:" in linea:
            detalles["Trastera"] = linea.split(":", 1)[-1].strip()
        elif "Micrófonos:" in linea:
            detalles["Micrófonos"] = linea.split(":", 1)[-1].strip()

    return detalles

def mostrar_guitarras_disponibles(monto_disponible):

    lista_guitarras = obtener_lista_guitarras()
    guitarras_disponibles = []

    for guitarra in lista_guitarras:
        if guitarra["precio"] <= monto_disponible:
            guitarras_disponibles.append(guitarra)

    if len(guitarras_disponibles) == 0:
        print("-------------------------------------------------")
        print("No hay guitarras disponibles para tu presupuesto.")
        print("-------------------------------------------------")
        return

    print("Guitarras disponibles:")
    for indice in range(len(guitarras_disponibles)):
        guitarra = guitarras_disponibles[indice]
        print(f"{indice + 1}. {guitarra['nombre']} - ${guitarra['precio']}")

    seleccion = int(input("Seleccione el número de la guitarra (0 para cancelar): "))
    if seleccion == 0:
        print("--------------------")
        print("Seleccion cancelada.")
        print("--------------------")
        return 

    if seleccion >= 1 and seleccion <= len(guitarras_disponibles):
        guitarra_seleccionada = guitarras_disponibles[seleccion - 1]
        detalles = obtener_detalles_guitarra(guitarra_seleccionada["ruta"])
        print(f"Detalles de {guitarra_seleccionada['nombre']}:")
        for clave in detalles:
            print(f"{clave}: {detalles[clave]}")
    else:
        print("---------------------")
        print("Seleccion incorrecta.")
        print("---------------------")
