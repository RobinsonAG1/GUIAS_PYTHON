class MascotaVirtual:
    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.energia: int = 10

    def jugar(self)->None:
        self.energia -= 3
        print(f"Estado actual despues de jugar: {self.energia}")
    
    def duerme(self)->None:
        self.energia += 5
        print(f"Estado actual despues de dormir: {self.energia}")

mascota = MascotaVirtual("Firulais")
mascota.jugar()
mascota.duerme()