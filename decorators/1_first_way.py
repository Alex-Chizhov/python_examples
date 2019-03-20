def dec(func):
    def wrap():
        new_list = []
        for i in func:
            new_list.append(i * 100)
        return new_list
    return wrap


def get_even_numbers(list):
    evens = []
    for i in list:
        if i % 2 == 0:
            evens.append(i)
    return evens

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Вызов самой функции
print(get_even_numbers(numbers))
# [2, 4, 6, 8, 10]

# Вызов задекорированной функции 1 способом
decorated_func = dec(get_even_numbers(numbers))
print(decorated_func())
# [200, 400, 600, 800, 1000]
