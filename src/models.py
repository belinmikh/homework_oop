class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float | int, quantity: int):
        if not isinstance(name, str):
            raise TypeError("A string was expected for the name")
        if not isinstance(description, str):
            raise TypeError("A string was excepted for the description")
        if (not isinstance(price, int) and not isinstance(price, float)) or price <= 0:
            raise TypeError("Positive number was expected for the price")
        if isinstance(price, int):
            price = float(price)
        if not isinstance(quantity, int):
            raise TypeError("An integer was expected for the quantity")
        if quantity < 0:
            raise ValueError("The quantity was expected to be non-negative")

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float | int) -> None:
        if (isinstance(price, int) or isinstance(price, float)) and price > 0:
            if price >= self.__price or input(
                "Вы уверены, что хотите понизить цену? "
                f"{self.__price} -> {price}\n"
                "(введите y для подтверждения)\n"
            ).lower().strip() in ["y", "у"]:
                self.__price = float(price)
        else:
            raise TypeError("Positive number was expected for the price")

    @classmethod
    def new_product(cls, product: dict): # how to type that?
        if not isinstance(product, dict):
            raise TypeError("Dictionary expected")
        try:
            return cls(product["name"], product["description"], product["price"], product["quantity"])
        except Exception as ex:
            raise TypeError(f"Bad dict format: {ex}")


class Category:
    # cls
    category_count: int = 0
    product_count: int = 0
    # obj
    name: str
    description: str
    __products: list[Product]

    def __init__(self, name: str, description: str, products: list[Product] | None = None):
        if not isinstance(name, str):
            raise TypeError("A string was expected for the name")
        if not isinstance(description, str):
            raise TypeError("A string was expected for the description")
        if products is None:
            products = []
        elif not isinstance(products, list):
            raise TypeError("A list was expected for the products")
        else:
            for p in products:
                if not isinstance(p, Product):
                    raise TypeError("Each item in products list was expected to be instance of Product class")

        Category.category_count += 1
        Category.product_count += len(products)

        self.name = name
        self.description = description
        self.__products = products

    def add_product(self, p: Product) -> None:
        if not isinstance(p, Product):
            raise TypeError("Product class object expected")
        self.__products.append(p)
        self.product_count += 1

    @property
    def products(self) -> str:
        result = []
        for p in self.__products:
            result.append(f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт.")
        return "\n".join(result)
