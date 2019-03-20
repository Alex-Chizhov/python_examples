def dec(func):                          # func
    def wrap(list):                     # arg
        new_list = []
        for i in func(list):            # function call with parameter
            new_list.append(i * 100)
        return new_list
    return wrap

@dec
def get_even_numbers(list):
    evens = []
    for i in list:
        if i % 2 == 0:
            evens.append(i)
    return evens


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(get_even_numbers(numbers))
# [200, 400, 600, 800, 1000]