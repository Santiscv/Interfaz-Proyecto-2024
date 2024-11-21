from instruments_details import obtener_lista_guitarras, obtener_detalles_guitarra ,mostrar_guitarras_disponibles

def menu():
    while True:
        try:
            monto_disponible = float(input("Ingrese el monto disponible (0 para salir): "))
            if monto_disponible == 0:
                print("Saliendo del programa.")
                break
            mostrar_guitarras_disponibles(monto_disponible)
        except ValueError:
            print("Por favor, ingrese un monto válido.")

if __name__ == "__main__":
    menu()