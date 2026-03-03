def calcular_salario_neto(salario_base: float, bonificacion: float = 0.0) -> float:

    descuento_salud = salario_base * 0.08
    descuento_pension = salario_base * 0.08

    salario_neto = salario_base - descuento_salud - descuento_pension + bonificacion

    return salario_neto


base = float(input("Ingrese el salario base: "))
bono = float(input("Ingrese la bonificación (si no hay, escriba 0): "))

resultado = calcular_salario_neto(base, bono)
print(f"El salario neto es: {resultado}")