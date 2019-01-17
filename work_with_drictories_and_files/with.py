# work with file using (try, except, finally)
f = open('./text_files/test.txt')
try:
    text = f.read()
    print(text)
except ValueError as e:
    print(e)
finally:
    f.close()


# using (with statement)
with open('./text_files/test.txt') as f:
    try:
        text = f.read()
        print(text)
    except ValueError as e:
        print(e)