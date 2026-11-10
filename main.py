from conexion import engine
from modelos import Base
from CRUD import crear_equipo, listar_equipos, buscar_equipo_por_id, actualizar_equipo, eliminar_equipos
from registros import registrar_estudiante, listar_estudiantes
from prestamos import registrar_prestamo

def main():
    Base.metadata.create_all(engine)
    
    while True:
        print("\n______MENÚ______")
        print("1. Crear equipo")
        print("2. Listar equipos")
        print("3. Buscar equipo por ID")
        print("4. Actualizar equipo")
        print("5. Eliminar equipo")
        print("6. Registrar estudiante")
        print("7. Listar estudiantes")
        print("8. Registrar préstamo")
        print("0. Salir")
        
        try:
            opcion = int(input("\nIngrese una opción: "))
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")
            continue

        if opcion == 1:
            nombre = input("Nombre del equipo: ").strip()
            tipo = input("Tipo de equipo: ").strip()
            try:
                stock = int(input("Stock disponible: "))
                crear_equipo(nombre, tipo, stock)
            except ValueError:
                print("Error: El stock debe ser un número entero válido.")

        elif opcion == 2:
            listar_equipos()

        elif opcion == 3:
            try:
                equipo_id = int(input("ID del equipo a buscar: "))
                buscar_equipo_por_id(equipo_id)
            except ValueError:
                print("Error: El ID debe ser un número entero válido.")

        elif opcion == 4:
            try:
                equipo_id = int(input("ID del equipo a actualizar: "))
                nombre = input("Nuevo nombre del equipo: ").strip()
                tipo = input("Nuevo tipo de equipo: ").strip()
                stock = int(input("Nuevo stock disponible: "))
                actualizar_equipo(equipo_id, nombre, tipo, stock)
            except ValueError:
                print("Error: Los datos numéricos deben ser enteros válidos.")

        elif opcion == 5:
            try:
                equipo_id = int(input("ID del equipo a eliminar: "))
                eliminar_equipos(equipo_id)
            except ValueError:
                print("Error: El ID debe ser un número entero válido.")

        elif opcion == 6:
            nombre = input("Nombre del estudiante: ").strip()
            correo = input("Correo del estudiante: ").strip()
            registrar_estudiante(nombre, correo)

        elif opcion == 7:
            listar_estudiantes()

        elif opcion == 8:
            try:
                estudiante_id = int(input("ID del estudiante: "))
                equipo_id = int(input("ID del equipo: "))
                fecha = input("Fecha (AAAA-MM-DD): ").strip()
                cantidad = int(input("Cantidad a prestar: "))
                registrar_prestamo(estudiante_id, equipo_id, fecha, cantidad)
            except ValueError:
                print("Error: Los IDs y la cantidad deben ser números enteros válidos.")

        elif opcion == 0:
            print("Saliendo del sistema...")
            break
        else:
            print("Error: Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()