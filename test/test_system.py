
import subprocess
import sys
from pathlib import Path


MAIN = Path(__file__).resolve().parents[1] / "main.py"


def ejecutar_programa(*argumentos):
    return subprocess.run(
        [sys.executable, str(MAIN), *map(str, argumentos)],
        capture_output=True,
        text=True,
        check=False
    )


def test_sistema_descuento():
    resultado = ejecutar_programa("descuento", 500, 20)

    assert resultado.returncode == 0
    assert resultado.stdout.strip() == "Resultado: 400.00"


def test_sistema_iva():
    resultado = ejecutar_programa("iva", 100)

    assert resultado.returncode == 0
    assert resultado.stdout.strip() == "Resultado: 116.00"


def test_sistema_error_precio_negativo():
    resultado = ejecutar_programa("descuento", -100, 10)

    assert resultado.returncode == 1
    assert "Error: El precio no puede ser negativo." in resultado.stdout


def test_sistema_porcentaje_invalido():
    resultado = ejecutar_programa("descuento", 100, 150)

    assert resultado.returncode == 1
    assert "El descuento debe estar entre 0 y 100." in resultado.stdout
