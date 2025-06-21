fruits = {
    "蘋果": 25,
    "香蕉": 20,
    "橘子": 30
}

while True:
    print("\n目前水果價格：")
    for name, price in fruits.items():
        print(f"{name}：{price}元")

    print("\n1. 查詢水果價格")
    print("2. 新增水果價格")
    print("3. 修改水果價格")
    print("4. 刪除水果")
    print("5. 離開系統")

    choice = input("請選擇功能（1–5）：")

    if choice == "1":
        name = input("請輸入要查詢的水果名稱：")
        if name in fruits:
            print(f"{name}的價格是 {fruits[name]}元")
        else:
            print("查無此水果")

    elif choice == "2":
        name = input("請輸入要新增的水果名稱：")
        if name in fruits:
            print(f"{name}已存在，價格是 {fruits[name]}元")
        else:
            price = int(input(f"請輸入{name}的價格："))
            fruits[name] = price
            print(f"{name}已新增，價格 {price}元")

    elif choice == "3":
        name = input("請輸入要修改的水果名稱：")
        if name in fruits:
            price = int(input(f"請輸入{name}的新價格："))
            fruits[name] = price
            print(f"{name}價格已修改為 {price}元")
        else:
            print("查無此水果")

    elif choice == "4":
        name = input("請輸入要刪除的水果名稱：")
        if name in fruits:
            fruits.pop(name)
            print(f"{name}已刪除")
        else:
            print("查無此水果")

    elif choice == "5":
        print("感謝使用水果店價格查詢系統！")
        break

    else:
        print("請輸入1~5之間的數字")