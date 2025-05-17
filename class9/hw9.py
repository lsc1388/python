"""
回家作業1
修改上課的練習程式，當使用者輸入數值時，程式不僅提示再大再小還需要提示縮小過後的輸入範圍
EX:
請輸入0~100的整數:50
再小一點
請輸入0~50的整數:25
再小一點
請輸入0~25的整數:15
再大一點
請輸入15~25的整數:30
再小一點
請輸入15~25的整數:10
再大一點
請輸入15~25的整數:20
再大一點
請輸入20~25的整數:23
再大一點
請輸入23~25的整數:24
恭喜猜中!
"""

import random

big = 100
small = 0
f = random.randint(1, 100)
while True:
    i = int(input("請輸入一個{small}到{big}到數字:"))
    if i == f:
        print("猜中了")
        break
    elif i < f:
        print("在小一點")
        if i < big:
            big = i
        elif i > small:
            small = i

        juices_list = ["蘋果汁", "柳橙汁", "葡萄汁", "系統關閉"]

while True:
    print("1. 蘋果汁")
    print("2. 柳橙汁")
    print("3. 葡萄汁")
    print("4. 系統關閉")

    choice = input("請輸入編號：")

    try:
        choice = int(choice)  # 直接嘗試轉換成數字
    except:
        print("輸入錯誤查無此果汁，請重新輸入\n")
        continue  # 失敗就請他重來

    if choice < 1 or choice > len(juices_list):
        print("輸入錯誤查無此果汁，請重新輸入\n")
        continue  # 超出選項範圍也請他重來

    if choice == 4:
        print("~~系統關閉~~")
        break

    print(f"您點的商品是 {juices_list[choice-1]}\n")
