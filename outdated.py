m = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
br = False
brb = False
while True:
    date = input("Дата: ").lower()
    a = False
    for mounth in m:
        if mounth in date:
            a = True
    if a:
        while True:
            b = date.split(' ')
            try:
                if int(b[0])<=31:
                    M = m.index(b[1])+1
                    D = int(b[0])
                    print(f"{b[2]}-{M:02}-{D:02}")
                    br = True
                    break
            except (ValueError, IndexError):
                break
            if br:
                break
    elif len(date.split(' '))!=3:
        while True:
            b = date.split('.')
            try:
                if int(b[0])<=31 and int(b[1])<=12:
                    D = int(b[0])
                    M = int(b[1])
                    print(f"{b[2]}-{M:02}-{D:02}")
                    br = True
                    break
                else:
                    break

            except (ValueError, IndexError):
                break
            if br:
                break
    elif len(date.split('.'))!=3:
        while True:
            b = date.split(' ')
            try:
                if int(b[0])<=31 and int(b[1])<=12:
                    D = int(b[0])
                    M = int(b[1])
                    print(f"{b[2]}-{M:02}-{D:02}")
                    br = True
                    break
                else:
                    break
            except (ValueError, IndexError):
                break
            if br:
                break
    if br:
        break