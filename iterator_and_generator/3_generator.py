# Генераторы позволяют упростить работу по конструированию итераторов
# Генератор – функция, которая будучи вызванной в функции next() возвращает следующий элемент согласно её алгоритму.
# Вместо ключевого слова return в генераторе используется yield.
# При вызове yield функция не прекращает работу, а “замораживается” до очередной итерации, запускаемой функцией next().

# Если вы в своем генераторе, где-то используете ключевое слово return,
# то дойдя до этого места будет выброшено исключение StopIteration,
# а если после ключевого слова return поместить какую-либо информацию, то она будет добавлена к описанию StopIteration.


def simple_generator(limit):
    item = 0
    while True:
        yield item
        item += 1
        if item >= limit:
            break

generator = simple_generator(5)

for i in generator:
    print(i)