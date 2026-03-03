nota = int(input("Ingrese su nota: "))

if nota < 0 or nota > 100:
    print("Nota no válida")
elif nota >= 60:
    print("Aprobado")
else:
    print("Reprobado")