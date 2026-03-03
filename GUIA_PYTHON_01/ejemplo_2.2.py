tiene_licencia = input("¿Tienes licensia de conducir? (si/no): ")
estado_sobrio = input("¿Has bebido alcohol hoy? (si/no): ")

if tiene_licencia == "si" and estado_sobrio == "no":
    print("Puedes conducir el vehiculo.")
else:
    print("Entregue las llaves. No puede conducir.")