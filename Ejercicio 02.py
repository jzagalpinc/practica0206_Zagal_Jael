#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje “<nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>”.

nombre = input("Ingrese su nombre por favor: ").capitalize()
edad = int(input("Ingrese su edad por favor: "))
direccion = input("Ingrese su dirección por favor: ").title()
telefono = int(input("Ingrese su número de teléfono por favor: "))
usuario = {
    "nombre":nombre,
    "edad":edad,
    "direccion":direccion,
    "telefono":telefono,
}
print(f"Su nombre es {usuario["nombre"]}, su edad es {usuario["edad"]}, su dirección es {usuario["direccion"]} y su teléfono es {usuario["telefono"]}")