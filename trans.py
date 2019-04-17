import json
with open('es.json', 'rb') as f:
    ext = json.load(f)
n = list(ext.keys())
d = {k:"" for k in n}
print(d)
with open('new.json', 'wb') as f:
    print(type(n))
    json.dump(d, f)