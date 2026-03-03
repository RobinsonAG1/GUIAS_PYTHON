class Servidor:

    def __init__(self, nombre: str, ip: str, ram: int):

        self.nombre: str = nombre
        self.ip: str = ip
        self.ram: int = ram
        self.estado: str = "Apagado"
    
server_ventas = Servidor("Ventas-01", "192.168.1.10", 16)
server_db = Servidor("Data-main", "10.0.0.5", 64)

print(f"El servidor {server_ventas.nombre} tiene {server_ventas.ram}GB de ram.")
print(f"El servidor {server_db.nombre} actualmente esta: {server_db.estado}")

        