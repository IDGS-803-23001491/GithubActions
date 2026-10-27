
import argparse
from tienda import calcular_precio, calcular_iva


def ejecutar_calculo(tipo, precio, porcentaje=None):
    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")

    if tipo == "descuento":
        if porcentaje is None or not 0 <= porcentaje <= 100:
            raise ValueError("El descuento debe estar entre 0 y 100.")

        return calcular_precio(precio, porcentaje)

    elif tipo == "iva":
        if porcentaje is None:
            porcentaje = 16

        if not 0 <= porcentaje <= 100:
            raise ValueError("El IVA debe estar entre 0 y 100.")

        return calcular_iva(precio)

    else:
        raise ValueError("Tipo de cálculo no válido.")


def main():
    parser = argparse.ArgumentParser(
        description="Calculadora de descuentos e IVA"
    )
    parser.add_argument("tipo", choices=["descuento", "iva"])
    parser.add_argument("precio", type=float)
    parser.add_argument("porcentaje", type=float, nargs="?")

    args = parser.parse_args()

    try:
        resultado = ejecutar_calculo(
            args.tipo, args.precio, args.porcentaje
        )
        print(f"Resultado: {resultado:.2f}")

    except ValueError as error:
        print(f"Error: {error}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
