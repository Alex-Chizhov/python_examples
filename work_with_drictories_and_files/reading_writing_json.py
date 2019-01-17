import json

f = open("text_files/example.json")
data = json.load(f)

print(type(data))
print(data)
f.close()