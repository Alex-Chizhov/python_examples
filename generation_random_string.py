import random
import string

random_letter = random.choice('abcd')
print(random_letter)

letters = string.ascii_letters
print(letters)

digits = string.digits
print(digits)

# with list comprehension
random_string = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(random.randint(1, 20))])
print(random_string)

# with for cycle
random_string_2 = ''
for i in range(random.randint(1, 20)):
    random_string_2 += str(random.choice(string.ascii_letters + string.digits))
print(random_string_2)