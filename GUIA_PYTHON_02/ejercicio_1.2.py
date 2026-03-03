def crear_perfil(nombre: str, rol : str) -> None:
    """Registrar un nuevo perfil en el sistema."""
    print(f"Regustrando en base de datos: {nombre} | Permisos: {rol}")

crear_perfil("Carlos", "Admin")
crear_perfil("Ana", "Ventas")


