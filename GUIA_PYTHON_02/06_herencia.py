class Empleado:
    def __init__(self, nombre: str, salario: float):
        self.nombre: str = nombre
        self.salario: float = salario

    def trabajar(self)->None:
        print(f"{self.nombre} está cumpliendo su horario regular.")

class Desarollador(Empleado):
    def programar(self) -> None:
        print(f"{self.nombre} está escribiendo código Python.")

class Gerente(Empleado):
    def trabajar(self)->None:
        print(f"{self.nombre} está en una reunión estratégica.")

dev = Desarollador("Carlos", 3500.0)
jefe = Gerente("Ana", 6000.0) 

dev.trabajar()
dev.programar()

jefe.trabajar()        