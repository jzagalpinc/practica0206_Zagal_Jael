#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

#Nota: El programa debe ser robusto y manejar errores de entrada y salida.

divisas = {"Euro":"€", "Dollar":"$", "Yen":"¥"}
while True:
    divisa = input("Ingrese su divisa por favor: ").capitalize().strip()
    if divisa in divisas:
        print(f"El símbolo de su divisa es {divisas[divisa]}")
        break
    else:
            print("Su divisa no se encuentra en la base de datos")
        








