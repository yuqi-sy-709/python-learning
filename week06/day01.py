# P5735 距离函数
from math import *
x1,y1=map(float,input().split())
x2,y2=map(float,input().split())
x3,y3=map(float,input().split())
def dis(a1,b1,a2,b2):
    return sqrt((a1-a2)**2+(b1-b2)**2)
d1=dis(x1,y1,x2,y2)
d2=dis(x1,y1,x3,y3)
d3=dis(x2,y2,x3,y3)
num=d1+d2+d3
print(f"{num:.2f}")