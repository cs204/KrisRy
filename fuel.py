d = 0
try:
    a = input("Дробь: ")
    for i in range(len(a)):
        if a[i]=='/':
            d = i
            break
    percent = (int(a[:d])/int(a[d+1:]))*100
except (ZeroDivisionError, ValueError):
    a = input("Дробь: ")
    for i in range(len(a)):
        if a[i]=='/':
            d = i
            break
    percent = (int(a[:d])/int(a[d+1:]))*100
if percent>100:
    a = input("Дробь: ")
    for i in range(len(a)):
        if a[i]=='/':
            d = i
            break
    percent = (int(a[:d])/int(a[d+1:]))*100
elif percent>=99:
    print("F")
elif percent<=1:
    print("E")
else:
    print(f'{int(percent)}%')