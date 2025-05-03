f = int(input("請輸入數字:"))
ans = "是質數"
for i in range(2, f):
    if f % i == 0:
        # 輸入數字除以迴圈變數,接著拿餘數來判斷是不是0,
        # 如果是0,則不是質數
        ans = "不是質數"

print(f"{f} {ans}")
