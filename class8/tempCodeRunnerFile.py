jump=int(input("請輸入要跳繩的數字:"))
for i in range(1,jump+1):
    if i % 10==0:
        print("休息1下")
        continue
    print(f"第{i}次跳繩")
