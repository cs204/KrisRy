amount = 0
coins = [5,10,20,50]
while amount<50:
    print(f"Нужная сумма: {50-amount}")
    coin = int(input("Вставьте монету: "))
    if coin in coins:
        amount += coin
    if amount < 50:
        print(f"Нужная сумма: {50-amount}")
    else:
        print(f"Ваша сдача: {amount-50}")