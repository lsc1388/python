n = input("請輸入數字")
n = int(n)  # 將輸入的數字轉換成整數
if n % 2 == 0:
    print(f"{n}是偶數")
else:
    print(f"{n}是奇數")

# 匯入模組
# import turtle#匯入模組turtle
import turtle as t  # 匯入模組turtle並取名為t

# from the turtle import *#匯入模組turtle的所有指令

# done()
# turtle.done()

# t.left(90)  # 向左移動90度
# t.back(100)  # 向移動100單位
t.speed(0)  # 設定速度為1
t.forward(100)  # 向前移動100單位
t.right(90)  # 向右移動90度
t.forward(100)  # 向前移動100單位
t.right(90)  # 向右移動90度
t.forward(100)  # 向前移動100單位
t.right(90)  # 向右移動90度
t.forward(100)  # 向前移動100單位
t.right(90)  # 向右移動90度
# 發現turtle一開始面秀邊
t.done()  # 讓視窗部要關閉

# for example
# for的組成有三部分
# for迴圈變數in範圍:
# 迴圈變數只能活在FOR迴圈裡面
# 迴圈變數每回合都會從範圍中取一個值
for i in range(6):  # range 可以產生一組數字,0-5
    print(i)

for j in range(1, 6):  # range  =1-5
    print(i)

for k in range(1, 6, 2):  # range =1,3,5
    print(i)


import turtle as t

t.speed(0)
for i in range(4):
    t.forward(100)
    t.right(90)

t.done()

import turtle

turtle.color("blue")  # 設定小烏龜顏色
turtle.shape("turtle")
# 設定小烏龜形狀'arrow', 'turtle', 'circle', 'square'triangle,claasic,.
turtle.stamp()  # 蓋章
turtle.stamp()  # 提筆

import turtle as t

t.penup()
t.color("red")
t.shape("turtle")
for i in range(100):
    t.forward(i * 2)
    t.stamp()
    t.right(40)
    speed(0)

    t.done()
