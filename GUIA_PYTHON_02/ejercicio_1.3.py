def calcular_iva(precio_base: float) -> float:
    """Calcular y retorna el precio total con un iva del 19%."""
    iva: float = precio_base * 0.19
    precio_final: float = precio_base + iva
    return precio_final 
factura_1: float = calcular_iva(10000.0)
factura_2: float = calcular_iva(50000.0)

print(f"Total a pagar factura 1: ${factura_1} ")
print(f"Total a pagar factura 1: ${factura_2} ")