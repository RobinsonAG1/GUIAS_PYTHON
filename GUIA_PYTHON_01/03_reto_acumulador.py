ACUM = 0

for producto in range(1, 6):
    pedido = float(input(f"Ingrese el valor del {producto}.producto: "))

    ACUM = ACUM + pedido

print(f"El valor a pagar por tus productos es: ${ACUM}")