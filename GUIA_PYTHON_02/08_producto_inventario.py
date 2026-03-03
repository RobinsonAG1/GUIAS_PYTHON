class Producto:
    def __init__(self, nombre: str, precio: float, stock: int):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def vender(self, cantidad: int)->None:
        try:
            if cantidad > self.stock:
                raise ValueError("Stock insuficiente")
            
            self.stock -=  cantidad
            print(f"Venta realizada. Stock restante: {self.stock}")
        
        except ValueError as error:
            print(f"Error: {error}")

class ProductoPerecedero(Producto):
    def __init__(self, nombre, precio, stock):
        super().__init__(nombre, precio, stock)
        self.dias_vencimiento = self.dias_vencimiento