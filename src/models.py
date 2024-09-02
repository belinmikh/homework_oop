class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float | int, quantity: int):
        if not isinstance(name, str):
            raise TypeError("A string was excepted for the name")
        if not isinstance(description, str):
            raise TypeError("A string was excepted for the description")
        if not isinstance(price, int) and not isinstance(price, float):
            # Not checking for a sign because negative
            # could be useful here (stocks as example)
            raise TypeError("A number was excepted for the price")
        if isinstance(price, int):
            price = float(price)
        if not isinstance(quantity, int):
            raise TypeError("An integer was expected for the quantity")
        if quantity < 0:
            raise ValueError("The quantity was expected to be non-negative")

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    # cls
    category_count: int = 0
    product_count: int = 0
    # obj
    name: str
    description: str
    products: list[Product]

    def __init__(self, name: str, description: str, products: list[Product] | None = None):
        if not isinstance(name, str):
            raise TypeError("A string was excepted for the name")
        if not isinstance(description, str):
            raise TypeError("A string was excepted for the description")
        if products is None:
            products = []
        elif not isinstance(products, list):
            raise TypeError("A list was expected for the products")
        else:
            for p in products:
                if not isinstance(p, Product):
                    raise TypeError("Each item in products list was expected " "to be instance of Product class")

        Category.category_count += 1
        Category.product_count += len(products)

        self.name = name
        self.description = description
        self.products = products
