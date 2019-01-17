# Reading
f = open('./work_with_drictories_and_files/test.txt')

text = f.read()
print(text)
f.close()

# Writing
f2 = open('./work_with_drictories_and_files/new_test.txt', 'w')
f2.write(text)
f2.close()