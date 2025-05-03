# 迴圈的break可以用來跳出所屬的迴圈,所以判斷break數與哪個迴圈時,必須要注意縮排
# 例如:

for i in range(5):
    for j in range(5):
        if i == 2 and j == 2:
            break
        print(f"i:{i},j:{j}")
        # 這裡的break只會跳出內層的for迴圈,外層的for迴圈還是會繼續執行只會跳出內層的for迴圈,外層的for迴圈還是會繼續執行

while True:
    print("1.蘋果汁 2.柳橙汁 3.葡萄汁 4.系統關閉")
    i = input("請輸入編號")
    if i == "1":
        print("顯示您點的商品是蘋果汁")
    elif i == "2":
        print("顯示您點的商品是柳橙汁")
    elif i == "3":
        print("顯示您點的商品葡萄汁")
    elif i == "4":
        print("顯示系統關閉")
        break
    else:
        print("輸入錯誤查無此果汁,請重新輸入")

        # continute
        # 迴圈的continue可以用來跳出當前的迴圈,繼續執行下次的迴圈
        # 例如:
for i in range(5):
    if i == 2:
        continue
    print(i)
    # 這裡的continue會跳過i=2的那次迴圈,直接執行i=3的那次迴圈
    # 所以輸入的結果是0,1,3,4
    # continue也可以用在while迴圈中
    # 例如:
    i = 0
    while i < 5:
        if i == 2:
            continue
print(i)
i += 1
# continue也要判斷所屬的迴圈,所以要注意縮排


# 輸入要跳繩的數字
jump = int(input("請輸入要跳繩的數字:"))
for i in range(1, jump + 1):
    if i % 10 == 0:
        print("休息1下")
        continue
    print(f"第{i}次跳繩")
