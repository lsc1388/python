"""
輸入一組整數範圍，將範圍中的所有質數顯示於畫面上。
EX：
請輸入開始整數:10
請輸入結束整數:50
11
13
17
19
23
29
31
37
41
43
47
"""

start = int(input("請輸入開始數字:"))
end = int(input("請輸入結束數字:"))
for n in range(start, end + 1):
    if n > 1:
        ans = "不是質數"
        for i in range(2, n):
            if n % i == 0:

                ans = "不是質數"
    if ans == "是質數":
        print(n)
