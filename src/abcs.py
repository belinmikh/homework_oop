from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @classmethod
    @abstractmethod
    def new_product(cls, product: dict):
        pass

    # other methods age magic, don't sure I should claim them
