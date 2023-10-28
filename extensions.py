a = input('File name: ')
b = ''
exts = ['.gif','.jpg','.jpeg','.png','.pdf','.txt','.zip']
mime = ['image/gif','image/jpeg','image/jpeg','image/png','application/pdf','text/plain','application/zip']
for i in range(-1,-len(a)-1, -1):
    b = a[i] + b
    if a[i] == '.':
        break
if b in exts:
    print(mime[exts.index(b)])
else:
    print('application/octet-stream')
