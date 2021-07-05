import hashlib
m = hashlib.md5()
text = 'sudhanshu ranjan'
m.update(text.encode('utf-8'))
print(m.hexdigest())
