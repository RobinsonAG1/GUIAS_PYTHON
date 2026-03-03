colores = ["Rojo", "Azul","Verde"]
usuario = input("Ingrese que color desea borrar: ")

if usuario in colores:
     colores.remove(usuario)
else:
     print("Color no valido")
print(colores)