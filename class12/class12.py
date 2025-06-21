# index 尋找指定元素 List中第一次出現的位置
# 如果元素不存在會產生錯誤,所以使用前先檢查元素是否存在
L = ["1", "2", "3", "4", "5"]
print(L.index("3"))  # 找到數字3在索引位置1

# count 統計某個元素在List中出現的次數
L = ["Hello", "World", "phython", "Hello"]
print(L.count("Hello"))  # "hello"這個字串總共出現2次

# sort 將List中的元素進行排序,預設是由小到大(升序排列)
# 注意:這個方法會ˋ直接修改原本的List,部會產生新的List
L[1, 3, 2, 4, 5]
L.sort()
print(L)


# split:將一個完整的字串按照指定的分隔符號切割成多部分
# 這是處理文字資料時非常常用的方法
s = "Hello," "World"
L = s.split(" ")  # 以空白字元作為分割點來切割字串
print(L)
calendar = "2020/12/25"
L = calendar.split("/")  # 以斜線作為分割點來切割日期字串

# join將List中的多個字串元素併成一個完整的字串
# 可以指定要用什麼符號來連接這些元素
L = ["Hello", "World"]
s = " ".join(L)  # 用空白字元將List中的元素連接成一個字串
print(s)
