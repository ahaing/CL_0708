#!/usr/bin/python3.10.2 (告訴別人這個檔案給哪一版本的python)
import random
min = 1 #建立一個猜數字1~100
max = 10
count = 0
target = random.randint(min, max)
# print(target) #要手動進入terminal (ctrl + shift + p)
print(f"猜數字遊戲{min}~{max}\n\n")

while True:
    keyin = int(input(f"猜數字遊戲{min}~{max}"))
    count += 1
    if (keyin == target):
        print(f" ~ BINGO! Congrats!!! The number is {target}~ ")
        print(f"猜了共{count}次")
    else:
        print("Sorry You Lose")
        print(f"猜錯第{count}次")
print("Game Over")
