from typing import Any

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
    assert c0.products == [p0, p1]


def test_category_init_empty() -> None:
    c0 = Category("name", "desc")
    assert c0.products == []
