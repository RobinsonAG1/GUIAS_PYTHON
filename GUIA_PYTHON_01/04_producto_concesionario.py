# Crear lista vacía
concesionario = []

# Ciclo para registrar 3 vehículos
for i in range(3):
    marca = input("Ingrese la marca del vehículo: ")
    modelo = input("Ingrese el modelo del vehículo: ")
    precio = input("Ingrese el precio del vehículo: ")

    # Crear diccionario temporal
    vehiculo = {
        "marca": marca,
        "modelo": modelo,
        "precio": precio
    }

    # Agregar el diccionario a la lista
    concesionario.append(vehiculo)

# Reporte de vehículos registrados.

for auto in concesionario:
    print(f"Vehículo registrado: Marca {auto['marca']}, Modelo {auto['modelo']}, Precio: ${auto['precio']}")
