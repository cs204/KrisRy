a = input()
b = a[0].lower()
for i in range(len(a)-1):
    if a[i+1].isupper():
        b = b+'_'+ a[i+1].lower()
    else:
        b = b + a[i+1]
print(f'Верблюжий стиль: {b}')