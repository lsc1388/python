# append 在程式執行的過程當中可以將資料加入到列表的最後面
L = ["hello", "world"]
L.append("phython")  # 加入phython
print(L)  # ['hello', 'world', 'phython']

# insert 在程式執行的過程當中可以將資料加入到列表的指定位置
L = ["hello", "world"]
L.insert(1, "phython")  # 在索引1的地方加入phython
print(L)  # ['hello', 'phython', 'world']

# 修改特定位置的資料
L = ["hello", "world"]
L[1] = "phython"  # 將索引1的資料改成phython
print(L)  # ['hello', 'phython']

print, weather = ["晴天", "多雲", "雨天", "晴天", "多雲", "雷陣雨","晴天"]
print weather

