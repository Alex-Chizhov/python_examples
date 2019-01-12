jack = {
    'age': '18',
    'size': 's'
}

john = {
    'age': '25',
    'size': 'l'
}

# list of dictionaries
users = [jack, john]
print(users)


# for
ages = []
for person in users:
    ages.append(person['age'])

print(ages)


# list comprehention
ages = [person['age'] for person in users]
print(ages)


# list comprehention 2
names = ['jack', 'john', 'andrew', 'jastin']
new_names = [name for name in names if name.startswith('j')]
print(new_names)