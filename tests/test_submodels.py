import pytest

from src.submodels import LawnGrass, Smartphone


def test_submodels_init() -> None:
    lg = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

    assert lg.country == "Россия"
    assert lg.germination_period == "7 дней"
    assert lg.color == "Зеленый"

    sp = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

    assert sp.efficiency == 90.3
    assert sp.model == "Note 11"
    assert sp.memory == 1024
    assert sp.color == "Синий"


def test_lawn_grass_init_raises() -> None:
    with pytest.raises(TypeError):
        LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, 123, "7 дней", "Зеленый")

    with pytest.raises(TypeError):
        LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", 123, "Зеленый")

    with pytest.raises(TypeError):
        LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", 123)


def test_smartphone_init_raises() -> None:
    with pytest.raises(TypeError):
        Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, "ABOBUS", "Note 11", 1024, "Синий")

    with pytest.raises(TypeError):
        Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, 123, 1024, "Синий")

    with pytest.raises(TypeError):
        Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", "ABOBUS", "Синий")

    with pytest.raises(ValueError):
        Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", -1024, "Синий")

    with pytest.raises(TypeError):
        Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, 123)
