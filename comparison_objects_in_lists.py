class Test:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'Test({self.a}, {self.b})'

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

list_1 = [Test(3, 2), Test(1, 4)]
list_2 = [Test(3, 2), Test(1, 4)]

assert list_1 == list_2