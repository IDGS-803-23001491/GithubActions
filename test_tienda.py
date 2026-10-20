import pytest
from tienda import calcular_precio, calcular_iva

def test_calcular_precio():
    assert calcular_precio(100,10) == 90

def test_calcular_iva():
    assert calcular_iva(100) == pytest.approx(118.0)

def test_calcular_sin_descuento():
    assert calcular_precio(500,0) == 500
