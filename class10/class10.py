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

weather = ["晴天", "多雲", "雨天", "晴天", "多雲", "雷陣雨", "晴天"]
print(weather)

while True:
    try:
        ans = int(input("要修改的星期數字(1~7："))
    except:
        print("請輸入數字編號")
    else:
        if ans > len(weather) or ans < 1:
            print("輸入錯誤查無此星期,請重新輸入")
        else:
            print("你要修改的星期是" + str(ans))
            print("原本的星期是+weather[ans-1]")
            new_weather = input("請輸入新的天氣：")
            weather[ans - 1] = new_weather
            print("修改後的天氣是" + weather[ans - 1])
            print(weather)
            break
