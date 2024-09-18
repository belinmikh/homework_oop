from src.mixins import MixinLog


def test_mixin_log(capsys):
    class TestClass(MixinLog):
        a: int
        b: str

        def __init__(self, a: int, b: str):
            self.a = a
            self.b = b

            super().__init__()

    TestClass(123, "test")

    captured = capsys.readouterr().out.split("\n")

    print(captured)

    assert captured[0].startswith("<tests.test_mixins.test_mixin_log.<locals>.TestClass object at")
    assert captured[1] == "\tkey a -> 123"
    assert captured[2] == "\tkey b -> 'test'"
