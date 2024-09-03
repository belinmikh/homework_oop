import json

from src.models import Category, Product


def read_json(path: str) -> list[Category]:
    with open(path, encoding="UTF-8") as file:
        data = json.load(file)
        result = [
            Category(
                c["name"],
                c["description"],
                [Product(p["name"], p["description"], p["price"], p["quantity"]) for p in c["products"]],
            )
            for c in data
        ]
    return result
