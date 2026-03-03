def es_mayor_de_edad(edad:int )->bool:
    return edad >= 18
edad_persona1: int = 21
edad_persona2: int = 14

if es_mayor_de_edad(edad_persona1):
    print("La persona uno es mayor de edad.")
else:
    print("La perosna dos no es mayor de edad")


if es_mayor_de_edad(edad_persona2):
    print("La persona doses mayor de edad.")
else:
    print("La persona dos no es mayor de edad")