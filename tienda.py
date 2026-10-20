def calcular_precio(precio, descuento):
    total = precio - (precio * descuento / 100)
    return total

def calcular_iva(precio):
    return round(precio * 1.16,2)

def validar_descuento(descuento):
    if descuento < 0 or descuento >= 100:
        raise ValueError("El decuento debe estar entre 0 y 100")
    return True