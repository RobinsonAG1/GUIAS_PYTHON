dias_semana = ("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")
usuario = int(input("Ingrese un numero del 1 al 7:  "))

if 1<= usuario <=7 :
    print(f"El dia es: {dias_semana[usuario -1]}")
else:
    print("Numero no valido")