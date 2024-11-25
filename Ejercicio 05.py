#Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas, hasta que el usuario introduzca la palabra “terminar”. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.

diccionario = {}
print("Introduce palabras en formato <español>:<inglés> separadas por comas.")
print("Por ejemplo: casa:house, perro:dog, gato:cat")
print("Escribe 'terminar' para finalizar la entrada del diccionario.")

while True:
    entrada = input("Introduce palabras (o 'terminar' para finalizar): ").strip()
    if entrada.lower() == "terminar":
        break
    else:
        try:
            pares = entrada.split(",")
            for par in pares:
                palabra, traduccion = par.split(":")
                diccionario[palabra.strip()] = traduccion.strip()
        except ValueError:
            print("Entrada inválida. Asegúrate de usar el formato <palabra>:<traducción>.")

print("\nDiccionario de traducción:")
for esp, eng in diccionario.items():
    print(f"{esp} -> {eng}")

frase = input("\nIntroduce una palabra en español para traducir: ").strip()
palabras = frase.split()
traduccion = []

for palabra in palabras:
    traduccion.append(diccionario.get(palabra, palabra))

frase_traducida = " ".join(traduccion)
print("\nPalabra traducida:")
print(frase_traducida)
