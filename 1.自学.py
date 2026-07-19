
""" 用python设计的第一个游戏
temp = input("请猜一下我现在心里想的是哪一个数字：")
guess = int(temp)
if guess == 8:
    print("你是我if x == 8:
        print("回答正确！")
else:
    if x < 8:
            print("猜小了！")
    else:
            print("猜大了！")肚子里的蛔虫吗？！")
    print("猜对了也没有奖励")
else:
    print("猜错了！我心想的是8！")
print("游戏结束！")

"""

"""
print(r"D:\three\two\one\now") 
"" r使转义字符失效""
print("I love China. \nI love Python.")

print (520+1314)
print ('520' + '1314')

num = 3
while num > 0:
    x = int(input("请输入一个数字："))

    if x == 8:
        print("回答正确！")
        break
    else :
        if x < 8:
            print("猜小了！")
        else:
            print("猜大了！")
    num -=1

import random
print(random.randint(1,10))
"""
import random
num = 3
answer = random.randint(1,10)
while num > 0:
    x = int(input("请输入你猜的数字："))
    if x == answer:
        print("回答正确！")
        break
    else:
        if x > answer:
            print("猜大了！")
        else:
            print("猜小了！")
    num -=1
print("游戏结束！")