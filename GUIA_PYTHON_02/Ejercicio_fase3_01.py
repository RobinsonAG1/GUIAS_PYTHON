class Vehiculo:
    def __init__(self, marca: str, modelo:  str, anio:int):

        self.marca: str = marca
        self.modelo: str = modelo
        self.anio: int = anio

auto_01 = Vehiculo("Nissan", "GTR", 2010)
auto_02 = Vehiculo("Toyota", "Prado", 2025) 

print(f"Auto 1: {auto_01.modelo}")
print(f"Auto 2: {auto_02.marca}")
    