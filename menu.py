from contactos import GestorContactos

# Muestra las opciones y retorna lo que elija el usuario
def mostrar_menu():
    print("\n--- Sistema de Gestión de Contactos ---")
    print("1. Agregar Contacto")
    print("2. Buscar Contacto")
    print("3. Editar Contacto")
    print("4. Eliminar Contacto")
    print("5. Listar Todos los Contactos")
    print("6. Salir")
    return input("Seleccione una opción: ")

def main():
    gestor = GestorContactos()

    while True:
        opcion = mostrar_menu()

        # Agregar: pide los datos y llama al gestor
        if opcion == '1':
            print("\n--- Agregar Contacto ---")
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            direccion = input("Dirección: ")
            exito, mensaje = gestor.agregar_contacto(nombre, telefono, email, direccion)
            print(mensaje)

        # Buscar: puede ser por nombre o telefono
        elif opcion == '2':
            print("\n--- Buscar Contacto ---")
            criterio = input("Buscar por (1) Nombre o (2) Teléfono: ")
            if criterio == '1':
                nombre = input("Ingrese el nombre a buscar: ")
                resultados = gestor.buscar_por_nombre(nombre)
                if resultados:
                    for c in resultados:
                        print(c)
                else:
                    print("No se encontraron contactos.")
            elif criterio == '2':
                telefono = input("Ingrese el teléfono a buscar: ")
                contacto = gestor.buscar_por_telefono(telefono)
                if contacto:
                    print(contacto)
                else:
                    print("Contacto no encontrado.")
            else:
                print("Opción inválida.")

        # Editar: busca por telefono y modifica lo que el usuario quiera
        elif opcion == '3':
            print("\n--- Editar Contacto ---")
            telefono_actual = input("Ingrese el teléfono del contacto a editar: ")
            print("Deje en blanco los campos que no desea modificar.")
            nombre = input("Nuevo Nombre: ") or None
            telefono_nuevo = input("Nuevo Teléfono: ") or None
            email = input("Nuevo Email: ") or None
            direccion = input("Nueva Dirección: ") or None

            exito, mensaje = gestor.editar_contacto(telefono_actual, nombre, telefono_nuevo, email, direccion)
            print(mensaje)

        # Eliminar: pide confirmacion antes de borrar
        elif opcion == '4':
            print("\n--- Eliminar Contacto ---")
            telefono = input("Ingrese el teléfono del contacto a eliminar: ")
            confirmacion = input(f"¿Está seguro de eliminar el contacto con teléfono {telefono}? (s/n): ")
            if confirmacion.lower() == 's':
                exito, mensaje = gestor.eliminar_contacto(telefono)
                print(mensaje)
            else:
                print("Operación cancelada.")

        # Listar: muestra todos o avisa si no hay
        elif opcion == '5':
            print("\n--- Lista de Contactos ---")
            contactos = gestor.listar_contactos()
            if contactos:
                for c in contactos:
                    print(c)
            else:
                print("No hay contactos registrados.")

        elif opcion == '6':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()