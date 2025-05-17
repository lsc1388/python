import random

big=100
small=0
f = random.randint(1, 100)
while True:
    i = int(input("請輸入一個{small}到{big}到數字:"))
    if i == f:
        print("猜中了")
        break
    elif i < f:
        print("在小一點")
        if i < big:
            big=i
        elif i > small:
               small=i