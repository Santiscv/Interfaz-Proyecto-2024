from instruments_details import obtener_lista_guitarras, obtener_detalles_guitarra ,mostrar_guitarras_disponibles

def menu():
    while True:
        try:
            print("Consultor de guitarras para Casa Libertella")
            print("----------------------------------------------------------------------")
            monto_disponible = float(input("Ingrese el monto disponible (0 para salir): "))
            print("----------------------------------------------------------------------")
            
            if monto_disponible == 0:
                print("----------------------")
                print("Saliendo del programa.")
                print("----------------------")
                break
            mostrar_guitarras_disponibles(monto_disponible)
        except ValueError:
            print("-----------------------------------")
            print("Por favor, ingrese un monto válido.")
            print("-----------------------------------")

if __name__ == "__main__":
    menu()