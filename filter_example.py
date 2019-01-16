my_list = [1, 2, 3, 4, 5]
new_list = list(filter(lambda i: i < 4, my_list))
print(new_list)


my_list = [2, 4, 'abc', 'sdn', None, None, 1, ' ', 'hello']
new_list = list( filter(lambda i: i!='hello',
                       filter(lambda i: i!= ' ',
                              filter(lambda i: i == str(i), my_list))) )
print(new_list)

my_list = [2, 4, 'abc', 'sdn', None, None, 1, ' ', 'hello']
new_list = list(filter(lambda i: i!='hello' and i!= ' 'and i == str(i), new_list))
print(new_list)