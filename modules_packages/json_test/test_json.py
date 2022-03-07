import json

fp = open("my_json.json", "w")

x = {"name": "naga", "age": 31, "height": 6.4,
     "good": True, "marks": [1, 2, 3, 4, 5], "hero": None}

json.dump(x, fp)

fp.close()

path = r"C:\Users\sRIKANTH\Downloads\sample2.json"
x = open(path, "r")

print(x)
y = json.load(x)
print(y)

x.close()
