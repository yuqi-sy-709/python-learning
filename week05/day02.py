# P5710 数的性质 （1)
x = int(input())
if x%2==0 and 4<x<=12:
    a = 1
else:
    a = 0
if x%2==0 or 4<x<=12:
    b = 1
else:
    b = 0
if (x%2==0 and not(4<x<=12)) or (x%2!=0 and 4<x<=12):
    c = 1
else:
    c = 0
if x%2!=0 and not(4<x<=12):
    d = 1
else:
    d = 0
print(a, b, c, d)

# P5711 闰年判断 (1)
x=int(input())
if (x%4==0 and x%100!=0)or (x%400==0):
    print("1")
else:
    print("0")

# P5716 月份天数 (1)
y,m=map(int,input().split())
if m in [1,3,5,7,8,10,12]:
    print(31)
elif m in [4,6,9,11]:
    print(30)
else:
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        print(29)
    else:
        print(28)