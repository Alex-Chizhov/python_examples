# Декоратор это функция которая изменяет поведение другой функции

def decor(func):
    def wrap():
        print('=====')
        func()
        print('=====')
    return wrap

# 1 способ задекорировать функцию
def print_hello():
    print('Hello')

decorated = decor(print_hello)
decorated()

# 2 способ
@decor
def print_hello():
    print('Hello')

print_hello()