class MixinLog:
    def __init__(self) -> None:
        print(
            f"{self.__repr__()} created:\n\t"
            + "\n\t".join([f"key {k} -> {v.__repr__()}" for k, v in vars(self).items()])
            + "\n"
        )

