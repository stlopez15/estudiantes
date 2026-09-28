import pytest

from src.citas import calcular_copago


def test_contributivo_paga_diez_por_ciento():
    assert calcular_copago(100000, "contributivo") == 10000


def test_subsidiado_no_paga():
    assert calcular_copago(100000, "subsidiado") == 0


def test_valores_invalidos_lanzan_error():
    with pytest.raises(ValueError):
        calcular_copago(-1, "particular")
    with pytest.raises(ValueError):
        calcular_copago(100000, "prepagada")
