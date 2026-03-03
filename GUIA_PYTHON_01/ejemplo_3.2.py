total_ahorrando = 0

for mes in range(1, 4):
    consignacion = int(input(f"¿Cuanto dinero vas ahorrar en el mes {mes} ?:"))
    total_ahorrando = total_ahorrando + consignacion
print(f"Ahorro completado! Tienes un total de: ${total_ahorrando}")

