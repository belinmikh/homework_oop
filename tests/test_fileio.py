from typing import Any
from unittest.mock import mock_open, patch

from src.fileio import read_json
from src.models import Category


@patch("builtins.open", new_callable=mock_open, read_data=None)
@patch("json.load")
def test_read_json(mock_load: Any, mock_file: Any) -> None:
    # while we aren't using __del__ or something
    Category.category_count = 0
    Category.product_count = 0

    mock_load.return_value = [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, "
            "но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, "
            "который позволяет наслаждаться просмотром, "
            "станет вашим другом и помощником",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        },
    ]

    data = read_json("file.json")

    mock_file.assert_called_once_with("file.json", encoding="UTF-8")

    assert Category.category_count == 2
    assert Category.product_count == 4

    assert data[0].name == "Смартфоны"
    # assert data[1].products[0].name == '55" QLED 4K'
    assert data[1].products.startswith('55" QLED 4K')
