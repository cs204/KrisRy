d = {"кофе": 20.00,
   "чай": 10.00,
   "булочка": 5.00,
   "салат": 30.40,
   "пирожное": 45.50}
cnt = 0
while True:
    try:
        cnt += d[input("Блюдо: ").lower()]
    except KeyError:
        continue
    except EOFError:
        print(f"\nСумма: {'%.2f' % cnt}")
        break