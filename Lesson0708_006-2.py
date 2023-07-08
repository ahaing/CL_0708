#!/usr/bin/python3.10.2 (告訴別人這個檔案給哪一版本的python)
import random
min = 1 #建立一個猜數字1~100
max = 10
count = 0
target = random.randint(min, max)
# print(target) #要手動進入terminal (ctrl + shift + p)
print(f"猜數字遊戲{min}~{max}\n\n")
while True
    while True:
        keyin = int(input(f"猜數字遊戲{min}~{max}:  "))
        count += 1
        if (keyin == target):
            print(f" ~ Congrats!!! The number is {target} ~ BINGO!! ~ ")
            print(f"== 猜了共{count}次 ==")
            break
        #
        elif keyin > target:
            print("smaller")
            max = keyin - 1
        #
        elif keyin < target:
            print("bigger")
            max = keyin + 1
        #
        #else:
        #    print("Sorry You're wrong")
            print(f"猜錯第{count}次\n")
    print("\n這局結束\n")
    againYN = input(f"\n請問是否還要繼續玩一次嗎?(Y/N)\n")
    break
    if againYN == N
    else
    
