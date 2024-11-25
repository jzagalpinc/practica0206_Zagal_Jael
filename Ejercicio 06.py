#Escribir un programa que permita gestionar la base de datos de alumnado de un classroom. Los alumnos y alumnas se guardarán en una lista que almacena un diccionario para cada alumno/a en el que la clave de cada alumno/a será su NIF, y el valor será otro diccionario con los datos del alumno/a (nombre, apellidos, teléfono, correo, aprobado), donde aprobado tendrá el valor True si ha aprobado el módulo. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir alumno/a, (2) Eliminar alumno/a, (3) Mostrar alumno/a, (4) Listar todo el alumnado, (5) Listar alumnado aprobado, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:
#Preguntar los datos del alumno/a, crear un diccionario con los datos y añadirlo a la base de datos.
#Preguntar por el NIF del alumno/a y eliminar sus datos de la base de datos.
#Preguntar por el NIF del alumno/a y mostrar sus datos.
#Mostrar lista de todo el alumnado de la base de datos con su NIF y nombre.
#Mostrar la lista del alumnado aprobado de la base de datos con su NIF y nombre.
#Terminar el programa.

base_datos = {}

def menu():
    print("\nMenú:")
    print("1. Añadir alumno/a")
    print("2. Eliminar alumno/a")
    print("3. Mostrar alumno/a")
    print("4. Listar todo el alumnado")
    print("5. Listar alumnado aprobado")
    print("6. Terminar")

def añadir_alumno():
    nif = input("Introduce el NIF del alumno/a: ").strip()
    if nif in base_datos:
        print("El NIF ya existe. No se puede añadir.")
        return
    nombre = input("Introduce el nombre: ").strip()
    apellidos = input("Introduce los apellidos: ").strip()
    telefono = input("Introduce el teléfono: ").strip()
    correo = input("Introduce el correo: ").strip()
    aprobado = input("¿Ha aprobado el módulo? (sí/no): ").strip().lower() == "sí"
    base_datos[nif] = {
        "nombre": nombre,
        "apellidos": apellidos,
        "telefono": telefono,
        "correo": correo,
        "aprobado": aprobado
    }
    print("Alumno/a añadido/a con éxito.")

def eliminar_alumno():
    nif = input("Introduce el NIF del alumno/a que deseas eliminar: ").strip()
    if nif in base_datos:
        del base_datos[nif]
        print("Alumno/a eliminado/a con éxito.")
    else:
        print("El NIF no se encuentra en la base de datos.")

def mostrar_alumno():
    nif = input("Introduce el NIF del alumno/a: ").strip()
    if nif in base_datos:
        print(f"Datos del alumno/a ({nif}):")
        for clave, valor in base_datos[nif].items():
            print(f"  {clave.capitalize()}: {valor}")
    else:
        print("El NIF no se encuentra en la base de datos.")

def listar_alumnado():
    if not base_datos:
        print("No hay alumnos/as en la base de datos.")
        return
    print("Listado de alumnado:")
    for nif, datos in base_datos.items():
        print(f"  NIF: {nif}, Nombre: {datos['nombre']} {datos['apellidos']}")

def listar_aprobados():
    aprobados = {nif: datos for nif, datos in base_datos.items() if datos["aprobado"]}
    if not aprobados:
        print("No hay alumnos/as aprobados/as.")
        return
    print("Listado de alumnado aprobado:")
    for nif, datos in aprobados.items():
        print(f"  NIF: {nif}, Nombre: {datos['nombre']} {datos['apellidos']}")

opcion = ""
while opcion != "6":
    menu()
    opcion = input("Selecciona una opción: ").strip()
    if opcion == "1":
        añadir_alumno()
    elif opcion == "2":
        eliminar_alumno()
    elif opcion == "3":
        mostrar_alumno()
    elif opcion == "4":
        listar_alumnado()
    elif opcion == "5":
        listar_aprobados()
    elif opcion == "6":
        print("Terminando el programa.")
    else:
        print("Opción no válida. Intenta de nuevo.")
