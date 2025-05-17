juices_list = ["蘋果汁", "柳橙汁", "葡萄汁", "可樂", "系統關閉"]

while True:
    print("1. 蘋果汁")
    print("2. 柳橙汁")
    print("3. 葡萄汁")
    print("4. 可樂")
    print("5. 系統關閉")
    
    choice = input("請輸入編號：")

    try:
        choice = int(choice)  # 嘗試轉換成數字
    except:
        print("輸入錯誤查無此飲料，請重新輸入\n")
        continue  # 轉換失敗就重來

    if choice < 1 or choice > len(juices_list):
        print("輸入錯誤查無此飲料，請重新輸入\n")
        continue  # 範圍錯誤也重來

    if choice == 5:
        print("~~系統關閉~~")
        break

    print(f"您點的商品是 {juices_list[choice-1]}\n")
