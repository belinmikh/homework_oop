from typing import Any
from unittest.mock import patch

import pytest

from src.models import Category, Product


@pytest.mark.parametrize(
    "name, description, price, quantity, test_ex",
    [
        (123, "desc0", 123, 123, TypeError),
        ("name1", 123, 123, 123, TypeError),
        ("name2", "desc2", "price2", 123, TypeError),
        ("name3", "desc3", 123, "quant3", TypeError),
        ("name4", "desc4", 123, 123.0, TypeError),
        ("name5", "desc5", 123, -123, ValueError),
        ("name6", "desc6", -123, 123, TypeError),
    ],
)
def test_product_init_raises(name: Any, description: Any, price: Any, quantity: Any, test_ex: Any) -> None:
    with pytest.raises(test_ex):
        Product(name, description, price, quantity)


def test_product_init() -> None:
    p = Product("bimbim", "bambam", 123, 123)

    assert p.name == "bimbim"
    assert p.description == "bambam"
    assert p.price == 123
    assert p.quantity == 123


@patch("builtins.input")
def test_product_price(input_mock: Any) -> None:
    input_mock.return_value = "y"

    p = Product("a", "b", 123, 123)

    p.price = 456
    assert p.price == 456

    with pytest.raises(TypeError):
        p.price = "a"

    with pytest.raises(TypeError):
        p.price = -123

    assert p.price == 456

    p.price = 123
    assert p.price == 123

    input_mock.return_value = "n"

    p.price = 38
    assert p.price == 123


def test_product_new_product() -> None:
    p = Product.new_product({"name": "a", "description": "b", "price": 123, "quantity": 123})

    assert p.name == "a"
    assert p.description == "b"
    assert p.price == 123.0
    assert p.quantity == 123

    with pytest.raises(TypeError):
        Product.new_product("abobus")

    with pytest.raises(TypeError):
        Product.new_product({"bimbim": "bambam"})


def test_product_str() -> None:
    p = Product("a", "b", 1, 2)
    assert str(p) == "a, 1.0 руб. Остаток: 2 шт."


def test_product_add() -> None:
    p0 = Product("a", "b", 2, 3)
    p1 = Product("c", "d", 4, 5)

    # 2 * 3 + 4 * 5 = 26
    assert p0 + p1 == 26
    # adding logic can be on purpose non-symmetric in some cases I believe
    assert p1 + p0 == 26

    with pytest.raises(TypeError):
        p0 + 123

    with pytest.raises(TypeError):
        "abobus" + p1


@pytest.mark.parametrize(
    "name, description, products, test_ex",
    [
        (123, "desc0", [Product("a", "b", 1, 1), Product("c", "d", 1, 1)], TypeError),
        ("name1", 123, [Product("a", "b", 1, 1), Product("c", "d", 1, 1)], TypeError),
        ("name2", "desc2", "abobus", TypeError),
        ("name3", "desc3", ["bimbim", "bambam"], TypeError),
    ],
)
def test_category_init_raises(name: Any, description: Any, products: Any, test_ex: Any) -> None:
    with pytest.raises(test_ex):
        Category(name, description, products)


def test_category_init_counts() -> None:
    # while we aren't using __del__ or something
    Category.category_count = 0
    Category.product_count = 0

    assert Category.category_count == 0
    assert Category.product_count == 0

    Category("name0", "desc0", [Product("a", "b", 1, 1), Product("c", "d", 1, 1)])

    assert Category.category_count == 1
    assert Category.product_count == 2

    Category("name1", "desc1", [Product("e", "f", 1, 1), Product("g", "h", 1, 1), Product("i", "j", 1, 1)])

    assert Category.category_count == 2
    assert Category.product_count == 5


def test_category_init_local() -> None:
    p0 = Product("a", "b", 1, 1)
    p1 = Product("c", "d", 1, 1)

    c0 = Category("name0", "desc0", [p0, p1])

    assert c0.name == "name0"
    assert c0.description == "desc0"
    # assert c0.products == [p0, p1]
    assert c0.products == "a, 1.0 руб. Остаток: 1 шт.\nc, 1.0 руб. Остаток: 1 шт."


def test_category_init_empty() -> None:
    c0 = Category("name", "desc")
    # assert c0.products == []
    assert c0.products == ""


def test_category_add_product() -> None:
    # while we aren't using __del__ or something
    Category.category_count = 0
    Category.product_count = 0

    c = Category("a", "b")

    assert Category.product_count == 0

    with pytest.raises(TypeError):
        c.add_product("abobus")

    assert Category.product_count == 0

    p = Product("a", "b", 123, 123)

    c.add_product(p)

    assert c.products == "a, 123.0 руб. Остаток: 123 шт."
    assert c.product_count == 1


def test_category_str() -> None:
    c = Category("a", "b", [Product("c", "d", 1, 2), Product("e", "f", 3, 4)])

    # 2 + 4 = 6
    assert str(c) == "a, количество продуктов: 6 шт."
