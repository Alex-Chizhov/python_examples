class Test:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'Test({self.a}, {self.b})'

my_list = [Test(3, 2), Test(1, 4)]

def a(obj):
    return obj.a

new_sorted_list = sorted(my_list, key=a)

# or with lambda
new_sorted_list = sorted(my_list, key=lambda obj: obj.a)
print(new_sorted_list)