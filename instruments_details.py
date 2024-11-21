import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.casalibertella.com/instrumentos-de-cuerdas/guitarras-electroacusticas/"

def obtener_sopa(url):
    """
    Realiza una solicitud HTTP y devuelve un objeto BeautifulSoup.
    """
    response = requests.get(url, timeout=10)
    return BeautifulSoup(response.text, "lxml")

def obtener_lista_guitarras():
    """
    Obtiene la lista de guitarras con nombre, ruta y precio desde la página principal.
    """
    soup = obtener_sopa(BASE_URL)
    precios = soup.select(".mt-0 .pecio_final b")
    titulos = soup.select(".card-title a")

    guitars = [
        {
            "nombre": title.text.strip(),
            "ruta": title['href'].split('/guitarras-electroacusticas/')[-1],
            "precio": float(precio.get_text(strip=True).replace("$", "").replace(",", ""))
        }
        for title, precio in zip(titulos, precios)
    ]
    return guitars

def obtener_detalles_guitarra(ruta):
    """
    Obtiene los detalles adicionales de una guitarra específica.
    """
    soup = obtener_sopa(BASE_URL + ruta)
    detalles = {"Origen": "no encontrado", "Trastera": "no encontrado", "Micrófonos": "no encontrado"}
    for linea in soup.select_one(".card-body").get_text(separator="\n").split("\n"):
        if "Origen:" in linea:
            detalles["Origen"] = linea.split(":", 1)[-1].strip()
        elif "Trastera:" in linea:
            detalles["Trastera"] = linea.split(":", 1)[-1].strip()
        elif "Micrófonos:" in linea:
            detalles["Micrófonos"] = linea.split(":", 1)[-1].strip()
    return detalles

def mostrar_guitarras_disponibles(monto_disponible):
    """
    Filtra y muestra guitarras dentro del presupuesto, permitiendo seleccionar una.
    """
    guitars = obtener_lista_guitarras()
    disponibles = [guitarra for g in guitars if g["precio"] <= monto_disponible]

    if not disponibles:
        print("No hay guitarras disponibles para tu presupuesto.")
        return

    print("Guitarras disponibles:")
    for i, guitarra in enumerate(disponibles, start=1):
        print(f"{i}. {guitarra['nombre']} - ${guitarra['precio']}")

    seleccion = int(input("Seleccione el número de la guitarra (0 para cancelar): "))
    if seleccion == 0:
        print("Selección cancelada.")
    elif 1 <= seleccion <= len(disponibles):
        seleccionada = disponibles[seleccion - 1]
        detalles = obtener_detalles_guitarra(seleccionada["ruta"])
        print(f"Detalles de {seleccionada['nombre']}:")
        for k, v in detalles.items():
            print(f"{k}: {v}")
    else:
        print("Selección inválida.")