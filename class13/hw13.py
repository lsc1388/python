fruits = {"蘋果": 28, "香蕉": 20, "橘子": 30}


while True:
    print("\n目前水果價格：")
    for name, price in fruits.items():
        print(f"{name}：{price} 元")

    print("\n水果店價格查詢系統")
    print("1. 新增水果價格")
    print("2. 修改水果價格")
    print("3. 刪除水果")
    print("4. 離開系統")

    choice = input("請選擇功能（1-4）：")

    if choice == "1":
        name = input("請輸入水果名稱：")
        if name in fruits:
            print(f"{name} 已存在，價格為 {fruits[name]} 元")
        else:
            price = int(input(f"請輸入 {name} 的價格："))
            fruits[name] = price
            print(f"{name} 已新增，價格為 {price} 元")

    elif choice == "2":
        name = input("請輸入要修改的水果名稱：")
        if name in fruits:
            price = int(input(f"請輸入新的價格："))
            fruits[name] = price
            print(f"{name} 的價格已更新為 {price} 元")
        else:
            print(f"{name} 不存在，無法修改")

    elif choice == "3":
        name = input("請輸入要刪除的水果名稱：")
        if name in fruits:
            fruits.pop(name)
            print(f"{name} 已刪除")
        else:
            print(f"{name} 不存在，無法刪除")

    elif choice == "4":
        print("感謝使用水果店價格查詢系統！")
        break

    else:
        print("請輸入正確選項（1-4）")
