class Base:
    def __init__(self) -> None:
        print("Base initializer")

    def f(self):
        print("Base.f()")


class Sub(Base):
    def __init__(self) -> None:
        super().__init__()
        print("Sub initializer")

    def f(self):
        print("Sub.f()")
    