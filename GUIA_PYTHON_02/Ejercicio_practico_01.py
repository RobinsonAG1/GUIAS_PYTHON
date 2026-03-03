def calcular_area_rectangulo(base: float, altura: float)-> None:
    op: float = base * altura 
    return op 

area_rentangulo1: float = calcular_area_rectangulo(4.2, 5.6)
area_rentangulo2: float = calcular_area_rectangulo(6.2, 3.0)

print(f"Area del rectangulo 1: {area_rentangulo1}")
print(f"Area del rectangulo 2: {area_rentangulo2}")

