import random  # 這是隨機模組

# random.randrange 設定範圍跟 range一樣,特性也一樣不包含最後一個數字
# random.randrange 的功能是隨機取得一個數字,range是產生一組數字
print(random.randrange(10))  # 從0到9隨機取得一個數字
print(random.randrange(1, 10))  # 從10到19隨機取得一個數字
print(random.randrange(1, 10, 2))  # 從[1,3,5,7,9]中隨機取得一個數字

# random.randint 設定範圍的方式必須要有開始跟結束,且包含最後一數字
# 不能跳數字抽籤
print(random.randint(1, 10))  # 從1到10隨機取得一個數字

import random

r = random.randint(1, 100)
while True:
    i = int(input("請輸入一個數字:"))
    if r == i:
        print("猜中了")
        break
    elif r < i:
        print("在小一點")
    else:
        print("在大一點")


# List 清單 (List)
# List 可以存入很多資料,每筆資料用ˋ,ˋ隔開
# List 可以存入不同型態的資料
# List 最外層用ˋ[]ˋ包起來
L = [1, 2, 3, 4, 5]  # 數字
print(L)
# 不同型態混和
L = [1, 2, 3, 4, 5, "hello", ["world", 6]]  # 數字,字串,List
print(L)

# List 取值
# List取值方式跟字串一樣,用ˋ{}ˋ取值
# List 取值方式跟字串一樣,也可以用ˋ[:]ˋ取值
# List 當中的資料的編號(index)都從0開始
L = [1, 2, 3, 4, 5]
print(L[0])  # 取得第一個值
print(L[1])  # 取得第二個值
print(L[2])  # 取得第三個值

# List 取值方式跟字串一樣,也可以用ˋ[:]ˋ取值
# 設定範圍的方式跟range很像,不包含最後一個數字
print(L[1:4:2])  # 取出第2個值到第4個值,且間隔為2
print(L[0:3])  # 取出第1個值到第3個值
print(L[3:])  # 取出第1個值到地3個值
print(L[3:])  # 取出第4個值到最後1個值
print(L[:])  # 取得全部值

# list len  列表長度
l = [1, 2, 3, 4, 5]
print(len(l))  # 取得List長度,也就是List當中有幾筆資料

# 務必不要跟index混淆,index是資料的編號,len是資料的數量

# len 可以搭配 for 迴圈使用來取得List當中的所有資料
for i in range(len(l)):  # 這邊的i是index
    print(L[i])
for i in l:  # 這邊的i是資料
    print(i)

    # 要使用哪一種方式讀取List當中的資料,要看使用的情境當中會部會需要index

    juices_list = ["蘋果汁", "柳橙汁", "葡萄汁", "系統關閉"]

while True:
    # 顯示清單選單
    for i in range(len(juices_list)):
        print(f"{i + 1}. {juices_list[i]}")

    # 輸入選項
    choice = input("請輸入編號：")

    # 檢查是否是數字
    if not choice.isdigit():
        print("輸入錯誤查無此果汁，請重新輸入\n")
        continue

    index = int(choice) - 1

    # 判斷選項是否在範圍內
    if 0 <= index < len(juices_list):
        if juices_list[index] == "系統關閉":
            print("~~系統關閉~~")
            break
        else:
            print(f"您點的商品是{juices_list[index]}\n")
    else:
        print("輸入錯誤查無此果汁，請重新輸入\n")
