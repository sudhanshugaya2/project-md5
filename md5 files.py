import hashlib
m = hashlib.md5()
text = 'hello world'
m.update(text.encode('utf-8'))
print(m.hexdigest())