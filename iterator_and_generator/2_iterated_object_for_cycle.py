# Если мы хотим, чтобы с данным объектом можно было работать в цикле for,
# то в класс SimpleIterator нужно добавить метод __iter__(),
# который возвращает итератор, в данном случае этот метод должен возвращать self.
# Объект этого класса становится итерируемым объектом


class SimpleIterator:

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration

obj = SimpleIterator(3)
for i in obj:
    print(i)