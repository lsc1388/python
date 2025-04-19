n = int(input("請輸入一個整數："))
for i in range(1, n + 1):
    if i % 3 == 0 or i % 7 == 0:
        print(i)

import turtle as t

t.speed(0)
t.penup()
for i in range(13):
    t.forward(100)
    t.stamp()
    t.home()
    t.right(30 * i)
t.done()

import turtle as t
import time

t.speed(0)
for j in range(60):
    t.right(6 * j)
    t.forward(80)
    time.sleep(1)
    t.home()
    t.clear()

    print(f" " * (n - i) + "*")
"""
請輸入要印出的箭頭大小
hint:
可利用字串乘法
>>>val="*" * 3
>>>print(val)
>>>***
EX:
請輸入要印出的箭頭大小:3
  *
 ***
*****
  *
  *
  *
"""

n = int(input("請輸入要印出的箭頭大小："))
for i in range(1, n + 1):
    print(f" " * (n - i) + "*" * (2 * i - 1))
for i in range(1, n + 1):
    print(f" " * (n - 1) + "*")
