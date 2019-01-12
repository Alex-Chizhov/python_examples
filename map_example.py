# convert list items via function

my_list = [1, 2, 3, 4, 5]
new_list = list(map(lambda i: i*2, my_list))
print(new_list)