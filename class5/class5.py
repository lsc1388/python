import turtle

# 設定畫布和畫筆
t = turtle.Turtle()
t.color("gold")
t.pensize(3)
t.speed(0)
turtle.fillcolor("yellow")
turtle.pencolor("yellow")


# 畫五角星
for i in range(5):
    t.forward(200)  # 向前畫一條邊（100像素）
    t.right(144)  # 每個轉角為144度，畫出星星形狀

# 結束
turtle.done()

turtle.home()  # 是讓烏龜回到原點的指令

turtle.clear()  # 清除畫面指令
import time  # 匯入模組time

time.sleep(1)  # 暫停1秒


x = int(input("請輸入一個整數："))
sum = 0
for i in range(x + 1):
    sum = sum + i
    print("從0加到" + str(x) + "的總總和為" + str(sum))

for i in range(1, 10):  # 外層迴圈，表示乘數
    for j in range(1, 10):  # 內層迴圈，被乘數
        print(f"{i} x {j} = {i*j}", end="\t")
    print()  # 換行
