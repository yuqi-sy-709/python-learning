# Day 2 作业：嵩天第二讲 - turtle蟒蛇绘制
# 先运行看效果，然后删掉代码自己重新敲一遍
from turtle import *
setup(150, 350, 200, 200)
penup()
fd(-50)
pendown()
seth(-40)
pensize(20)
pencolor("blue")
for i in range(4):
    circle(40,80)
    circle(-40,80)
circle(40,40)
fd(40)
circle(16,180)
fd(40*2/3)
done()