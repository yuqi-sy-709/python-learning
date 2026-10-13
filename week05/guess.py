
from random import randint
n=randint(1,100)
for i in range(1,101):
    d=int(input("请输入一个整数："))
    if d>n:
        print("你猜的数大了")
    elif d<n:
        print("你猜的数小了")
    else:
        print("恭喜你猜对了")
        break
