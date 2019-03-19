# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Syntax
# lambda arguments : expression

x = lambda a: a + 10
print(x(5))
# 15

x = lambda a, b: a * b
print(x(2, 3))
# 6

x = lambda a, b, c: a + b + c
print(x(1, 1, 1))
# 3

x =lambda x: 'positive' if x > 0 else 'negative'
print(x(-1))
# negative


# The power of lambda is better shown when you use them as an anonymous function inside another function.
def my_func(n):
    return lambda a: a * n

multiplication = my_func(2) # n = 2
print(multiplication(11))   # a = 11
# 22