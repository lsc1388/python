# try except
# 錯誤處理
try:
    # 嘗試執行可能會出錯的程式碼
    n = int(input("inout a number:"))

except:
    # 如果有錯誤發生,執行這個程式碼
    print("請輸入有效的數字")

else:
    # 如果沒有錯誤發生,執行這個程式碼
    print(n + 1)


try:
    h = float(input("請輸入身高:"))
    w = float(input("請輸入體重:"))
    bmi = w / h**2
    print(f"你的bmi為:  {bmi}")
except:
    print("請輸入有效的數字")
    print("請輸入有效的數字")


# 比較運算子
print(1 == 1)  # True, 1等於1
print(1 != 1)  # False, 1不等於1
print(1 > 1)  # False, 1不大於1
print(1 < 1)  # False, 1不小於1
print(1 >= 1)  # True, 1大於等於1
print(1 <= 1)  # True, 1小於等於1
# 邏輯運算子
# and 代表全部條件都要成立才會回傳true
# or 代表只要一個條件成立就就會回傳false
# not 代表將原本的布林值反轉

print(True and True)  # True
print(True and False)  # False, True和False
print(False and False)  # False, False和false
print(False and False)  # False, False和False
print(True or True)  # True, True或True
print(True or False)  # True, True或False
print(not True)  # False, 非True
print(not False)  # True, 非False


password = input("請輸入密碼:")
if  password== "1234":
    print("密碼正確")
else:
    print("密碼錯誤")

    #if elif else
   elif pwd == "1234":#如果密碼是\1234
print("密碼正確")#印出密碼正確
else:
print("密碼錯誤")

#if elif else是連續的判斷,只要有一個條件成立後面的判斷就部會執行
# if 一定要有,elif可以有多個但是選用,else只能有一個但是選用
if 分數>90:
    print("a")
elif 分數 80-90:
    print("b")
elif 分數 70-79:
    print("c")
elif 分數 60-69:
    print("d")
elif 分數<59:
    print("e")
