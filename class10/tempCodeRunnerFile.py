weather = ["晴天", "多雲", "雨天", "晴天", "多雲", "雷陣雨","晴天"]
print (weather)

while True:
    try:
        ans=int(input("要修改的星期數字(1~7："))
    except:
        print("請輸入數字編號")
    else:
        if ans > len(weather) or ans < 1:
            print("輸入錯誤查無此星期,請重新輸入")
        else:
            print("你要修改的星期是"+ str(ans))
            print ("原本的星期是+weather[ans-1]")
            new_weather=input("請輸入新的天氣：")
            weather[ans-1]=new_weather
            print("修改後的天氣是"+weather[ans-1])
            print(weather)
            break                                                           
