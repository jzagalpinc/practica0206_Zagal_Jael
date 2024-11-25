#Escribir un programa que guarde en un diccionario los precios de los artículos de la tabla, pregunte al usuario por un artículo, un número de unidades y muestre por pantalla el precio de esa cantidad de producto. Si el producto no está en el diccionario debe mostrar un mensaje informando de ello.

productos = {
    "Pan":1.40,
    "Huevos":2.30,
    "Cebolla":0.85,
    "Aceite":4.35
    }

print("¡Llene su canasta!")
for articulo, precios in productos.items():
    print(f"{articulo}: {precios:.2f}€")
    
while True:
    canasta = input("Ingrese el producto deseado: ").strip().capitalize()
    if canasta in productos:
        while True:
            try:
                unidades = input("Ingrese las unidades deseadas: ").strip()
                unidades = int(unidades)
                total = unidades * productos[canasta]
                print(f"El precio por {unidades} unidades del producto '{canasta}' es : {total:.2f}€")
                break
            except ValueError:
                print("El número de unidades debe ser un valor entero.") 
        break
    else:
        print("El producto no se encuentra disponible.")

