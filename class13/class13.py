# 字典(Dictionary):用來儲存[key-value]配對的資料結構
# 字典很適合用來表示有對應關係的資料,像是商品和價格的對應

# 建立字典:是用大括號{},key和value之間用冒號:分隔
d = {"蘋果:20", "香蕉:30", "橘子:25"}
print(d)

# 從字典中取得特定key對應的value
# 如果key不存在會產生KeyError錯誤
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print(d["蘋果"])
# print(d["梨子"])#這行會產生KeyError:'梨子'錯誤

# 遍歷字典:有多種方式可以走訪字典中的資料
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}

# 方式1:直接遍歷字典,會取得所有的Key
for k in d:
    print(k)  # 印出Key名稱
    print(d[k])  # 用Key來取得對應的Value

    # 方式2:明確使用Keys()方法來取得所有Key
for k in d.keys():
    print(k)  # 印出Key名稱
    print(d[k])  # 用Key來取得對應的Value

    # 方式3:使用Values()方法來取得所有Value
    for v in d.values():
        print(v)  # 直接印出Value但不知道對應的Key是什麼

        # 方式4:使用Items()方法同時取得Key和Value
        # 這是最常用的方式,因為可以同時存取Key和Value
        for k, v in d.items():
            print(f"{k}:{v}")  # 同時印出Key和Value的配對關係

# 新增/修改字典的內容
# 直接指定Key對應的Value,如果Key已存在就是修改,如果Key不存在就是新增
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
d["蘋果"] = 10  # 修改蘋果對應的Value
print(d)
d["蓮霧"] = 15  # 新增一個Key-Value配對
print(d)

# 刪除字典中的內容
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
d.pop("蘋果")  # 刪除蘋果
# 如果刪掉的Key不存在,會出現KeyError,所以可以加上第二個參數,Key不存在時,不會有任何變化
popitem = d.pop("蓮霧", "不存在這筆資料")  # 不會有任何變化
print(d)  # {'香蕉': 30, '橘子': 25}
print(popitem)  # 不存在這筆資料


# len:取得字典中有多少組Key-Value配對
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print(len(d))


# 檢查某個Key是否存在於字典中
# 使用前先檢查可以避免KeyError錯誤
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print("蘋果" in d)  # True,蘋果這個Key存在
print("蓮霧" in d)  # False,蓮霧這個Key不存在


# 檢查某個元素有沒有在List中
# 使用in可以快速檢查某個元素是否存在
L = [1, 2, 3, 4, 5]
print(3 in L)  # True,3在List中
