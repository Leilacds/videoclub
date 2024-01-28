#--- Menu Principal ---
def menu_principal():
    while True:
        print("----- MenúPrincipal -----")
        print("0 - Consulta de disponibilidad")
        print("1 - Préstamo de Película")
        print("2 - Gestión del cliente")
        print("3 - Gestión de Película")
        print("4 - Salir")
        opcion = input("Seleccione una opción: ")
        menu_options = {
            "0": consulta_disponibilidad_menu,
            "1": submenu_prestamo,
            "2": submenu_gestion_cliente,
            "3": submenu_gestion_pelicula,
            "4": salir_menu
        }

        if opcion in menu_options:
            menu_options[opcion]()
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")



#--- Sub menus ---
# Función para opción 0 consulta_disponibilidad_menu
def consulta_disponibilidad_menu():
    print("Ingresando consulta_disponibilidad_menu...")

# Función para opción 1 submenu_prestamo
def submenu_prestamo():
    print("Ingresando Préstamo de Película...")

# Función para opción 2 submenu_gestion_cliente
def submenu_gestion_cliente():
    print("Ingresando submenu_gestion_cliente...")

# Función para opción 3 submenu_gestion_pelicula
def submenu_gestion_pelicula():
    print("Ingresando submenu_gestion_pelicula...")

# Función para opción 4 salir del programa
def salir_menu():
    print("Saliendo del programa...")
    exit()


# Llama a la función del menú principal para iniciar la aplicación
menu_principal()