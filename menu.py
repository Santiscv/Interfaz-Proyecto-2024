from instruments_details import obtener_lista_guitarras, obtener_detalles_guitarra

def mostrar_guitarras_disponibles(monto_disponible):
    guitars_list = obtener_lista_guitarras(urlPagina="https://www.casalibertella.com/instrumentos-de-cuerdas/guitarras-electroacusticas/")
    disponibles = [guitarra for guitarra in guitars_list if guitarra["precio"] <= monto_disponible]
    
    if disponibles:
        print("Guitarras disponibles para tu presupuesto:")
        for id, guitarra in enumerate(disponibles, start=1):
            print(f"{id}. Nombre: {guitarra['nombre']}, Precio: ${guitarra['precio']}")
        
        while True:
            try:
                seleccion = int(input("Seleccione el número de la guitarra que desea (o '0' para cancelar): "))
                if seleccion == 0:
                    print("Cancelando selección.")
                    break
                elif 1 <= seleccion <= len(disponibles):
                    guitarra_seleccionada = disponibles[seleccion - 1]
                    print(f"Has seleccionado: {guitarra_seleccionada['nombre']} por ${guitarra_seleccionada['precio']}")
                    
                    # Obtener detalles adicionales
                    detalles = obtener_detalles_guitarra(guitarra_seleccionada['ruta'])
                    print("Detalles adicionales:")
                    print(f"--------------------")
                    print(f"Origen: {detalles['Origen']}")
                    print(f"--------------------")
                    print(f"Trastera: {detalles['Trastera']}")
                    print(f"--------------------")
                    print(f"Micrófonos: {detalles['Micrófonos']}")
                    print(f"--------------------")
                    break
                else:
                    print("Selección no válida. Intente de nuevo.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
    else:
        print("No hay guitarras disponibles para tu presupuesto.")

def menu():
    while True:
        try:
            monto_disponible = float(input("Ingrese el monto disponible (o '0' para salir): "))
            if monto_disponible == 0:
                print("Saliendo del programa.")
                break
            mostrar_guitarras_disponibles(monto_disponible)
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    menu()
