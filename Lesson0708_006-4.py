#!/usr/bin/python3.10.2 (告訴別人這個檔案給哪一版本的python)
# .py檔時，要手動(ctrl + shift + p)，進入terminal 執行程式

import random
def playGame():
    minIN = int(input(f" [猜數字遊戲] 請輸入下限數字: "))
    maxIN = int(input(f" [猜數字遊戲] 請輸入上限數字: "))
    # min = 1 #建立一個猜數字1~100
    # max = 10
    count = 0
    target = random.randint(minIN, maxIN)
    # target = random.randint(min, max)
    print(f"洩題:{target}") 
    #print(f"猜數字遊戲{min}~{max}\n\n")

    while True:
        keyin = int(input(f"猜數字遊戲{minIN}~{maxIN}:  "))
        count += 1
        if (keyin == target):
            print(f" ~ BINGO!! ~ \n ~ The number is {target} ~ Congrats!!! ")
            print(f"== 猜了共{count}次 ==")
            break
        #
        elif keyin > target:
            print("> smaller")
            max = keyin - 1
        #
        elif keyin < target:
            print("< bigger")
            max = keyin + 1
        #
        #else:
        #    print("Sorry You're wrong")
        print(f"=> 猜錯第{count}次\n")    

while(True):
    playGame()
    play_again = input ("\nstart again? (Y/N)")
    if (not play_again == 'Y'):
        break
print("==Game Over==\n")