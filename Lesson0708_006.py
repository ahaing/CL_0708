#!/usr/bin/python3.10.2 (告訴別人這個檔案給哪一版本的python)
import random
min = 1 #建立一個猜數字1~100
max = 10
count = 0
target = random.randint(min, max)
# print(target) #要手動進入terminal (ctrl + shift + p)
print(f"猜數字遊戲{min}~{max}\n\n")

while True:
    keyin = int(input(f"猜數字遊戲{min}~{max}:"))
    count += 1
    if (keyin == target):
        print(f" ~ Congrats!!! The number is {target} ~ BINGO!! ~ ")
        print(f"== 猜了共{count}次 ==")
        break
    else:
        print("Sorry You're wrong")
        print(f"猜錯第{count}次\n")
print("\nGame Over\n")
