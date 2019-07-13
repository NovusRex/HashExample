import hashlib

value = 'x'
hans = hashlib.sha512()
hans.update(str(value).encode('utf-8'))
print(hans.hexdigest())

print('-----------------')
