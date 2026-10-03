#==============圆的面积=================
import math
r=float(input())
s=math.pi*r**2
print("{0:.2f}".format(s))
#==============向上买箱==================
import math
n=int(input())
print(math.ceil(n/12))
#==============平均分取整================
import math
a,b,c=map(int,input().split())
avg=(a+b+c)/3
print(math.ceil(avg))
#注意跟int（）和round()的区别
print(int(avg))
print(round(avg))
#==============两点距离================
import math
x1,y1,x2,y2=map(int,input().split())
d=math.sqrt((x2-x1)**2+(y2-y1)**2)
print("{0:.2f}".format(d))
#==============三角斜边================
import math
a,b=map(int,input().split())
c=math.hypot(a,b)
print("{0:.2f}".format(c))
