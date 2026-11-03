
import pytest
from main import ejecutar_calculo


def test_integracion_descuento():
    resultado = ejecutar_calculo("descuento", 500, 20)
    assert resultado == pytest.approx(400)


def test_integracion_iva():
    resultado = ejecutar_calculo("iva", 100)
    assert resultado == pytest.approx(116)


def test_integracion_tipo_invalido():
    with pytest.raises(ValueError, match="Tipo de cálculo"):
        ejecutar_calculo("recargo", 100, 10)


def test_integracion_precio_negativo():
    with pytest.raises(ValueError, match="negativo"):
        ejecutar_calculo("descuento", -100, 10)
