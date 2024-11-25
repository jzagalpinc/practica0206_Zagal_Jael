#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
usuario = {}
usuario["nombre"] = input("Por favor ingrese su nombre: ").strip().title()
print(f"Nombre: {usuario['nombre']}")
while True:
    try:
        usuario["edad"] = input("Ingrese su edad por favor: ").strip()
        usuario["edad"] = int(usuario["edad"])
        print(f"Edad: {usuario['edad']}")
        break
    except:
        print("Tu edad debe ser un número entero.")
usuario["sexo"] = input("Ingrese su sexo por favor: ").strip().capitalize()
print(f"Sexo: {usuario['sexo']}")
while True:
    try:
        usuario["telefono"] = input("Ingrese su número de teléfono: ").strip()
        usuario["telefono"] = int(usuario["telefono"])
        print(f"Teléfono: {usuario["telefono"]}")
        break
    except:
        print("El número de teléfono debe ser un valor entero")
usuario["correo"] = input("Ingrese su correo: ").strip()
print(f"Correo electronico: {usuario['correo']}\n")

print(f"""Información completa del usuario:\n
Nombre: {usuario['nombre']}
Edad: {usuario['edad']}
Sexo: {usuario['sexo']}
Teléfono: {usuario['telefono']}
Correo electrónico: {usuario['correo']}""")
