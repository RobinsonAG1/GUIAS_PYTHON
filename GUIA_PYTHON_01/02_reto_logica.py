usuario_estatura = float(input("¿Cual es tu estarura?: "))
usuario_edad = int(input("¿Que edad tienes?: "))

if usuario_estatura >= 1.50 and usuario_edad >= 12:
    print("Permitido.")
else:
    print("Denegado.")