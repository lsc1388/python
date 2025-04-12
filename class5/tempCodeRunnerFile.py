for i in range(1, 10):          # 外層迴圈，表示乘數
    for j in range(1, 10):      # 內層迴圈，被乘數
        print(f"{i} x {j} = {i*j}", end="\t")
    print()  # 換行

