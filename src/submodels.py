from src.models import Product


class Smartphone(Product):
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float | int,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        if not isinstance(efficiency, float):
            raise TypeError("Float expected for the efficiency")
        if not isinstance(model, str):
            raise TypeError("String expected for the model")
        if not isinstance(memory, int):
            raise TypeError("Integer expected for the memory")
        if memory <= 0:
            raise ValueError("Positive value expected for the memory")
        if not isinstance(color, str):
            raise TypeError("String expected for the color")

        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float | int,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        if not isinstance(country, str):
            raise TypeError("String expected for country")
        if not isinstance(germination_period, str):
            raise TypeError("String expected for germination_period")
        if not isinstance(color, str):
            raise TypeError("String expected for color")

        self.country = country
        self.germination_period = germination_period
        self.color = color
