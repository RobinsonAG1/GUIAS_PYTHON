carrito_compras = ["Leche","Huevos","Pan"]
print("Carrito inicial. {carrito_compras}")

carrito_compras.append("Café")
print(f"Agregue Café: {carrito_compras}")

carrito_compras.remove("Leche")
print(f"Quité la leche: {carrito_compras}")

#cambiar un elemento sabiendo su posicion
carrito_compras[0] = "Huevos Campesinos"
print(f"Cambie los huevos normales: {carrito_compras}")
