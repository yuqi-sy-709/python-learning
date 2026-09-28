#===================算术运算符====================
a,b=map(int,input().split())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

#===================天天向上====================
dayfact=1
dayup=pow(1+dayfact,365)
daydown=pow(1-dayfact,365)
print("向上：{:.2f} 向下：{:.2f}".format(dayup,daydown))