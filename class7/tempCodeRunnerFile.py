start = int(input("請輸入開始數字:"))
end=int(input("請輸入結束數字:"))
for n in range(start, end + 1):
    if n > 1:
     ans = "不是質數"
     for i in range(2, n):
          if n  % i == 0:
        # 輸入數字除以迴圈變數,接著拿餘數來判斷是不是0,
        # 如果是0,則不是質數
            ans = "不是質數"
    if ans == "是質數":
            print(n)