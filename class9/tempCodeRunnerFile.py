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