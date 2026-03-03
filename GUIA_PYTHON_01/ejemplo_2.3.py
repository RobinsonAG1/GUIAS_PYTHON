print("---Diagnósico de Red---")
hay_internet = input("¿El módem tiene luces encendidas? (si/no): ")

if hay_internet == "si":
    print("Paso 1: El equipo recibe energia.")
    
    luz_roja = input("¿Algunas de las luces es color ROJO?? (si/no): ") 
    if luz_roja == "si":
        print("Fallo detectado: Problema en la fibra optica. Llame a soporte.")
    else:
        print("Todo normal: Su conexion esta operando al 100%.")

else:
    print("Fallo critico: Verifique que el equipo esté conectado a la corriente.")