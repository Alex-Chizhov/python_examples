# Итератор объект перечеслитель
# - выдает следующий элемент последовательности при помощи next()
# - выбрасывает исключение если элементы закончмлмсь
# - класс объекта итератора должен иметь метод __next__()


class SimpleIterator:

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration

obj = SimpleIterator(3)
print(next(obj))
print(next(obj))
print(next(obj))
