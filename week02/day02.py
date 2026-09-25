from turtle import *
penup()
fd(-50)
pendown()
seth(0)
pensize(10)
pencolor("red")
for i in range(4):
    fd(100)
    rt(90)

#=== 画六边形 ===
penup()
goto(150, 0)  
pendown()
pensize(10)
pencolor("blue")
for i in range(6):
    fd(60)
    rt(60)
done()  