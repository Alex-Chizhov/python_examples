class MyClass:

    def __init__(self):
        self.a = 10
    @staticmethod
    def addition(x, y):
        ''' Этот статический метод, будет доступен даже без создания экземпляра класса.
        В статический метод не передается self (ссылка но объект), и доступа к объекту следовательно нет '''
        return x + y

    @classmethod
    def subtraction(cls, x, y):
        '''В качестве первого параметра в метод класса передается ссылка на класс'''
        return x - y



''' Вызов статического метода '''
# 1.Через класс
answer = MyClass.addition(2, 3)
print(answer)
# 5

# 2.Через экземпляр класса
obj = MyClass()
print(obj.addition(6, 4))
# 10

''' Вызов метода класса '''
# 1.Через класс
answer = MyClass.subtraction(5, 2)
print(answer)
# 3

# 2.Через экземпляр класса
obj = MyClass()
print(obj.subtraction(10, 6))
# 4


