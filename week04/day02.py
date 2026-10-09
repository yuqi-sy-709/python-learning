# format格式化
n,a = "haha", 19
print("{}今年{}岁".format(n,a))
print("{0}今年{1}岁".format(n,a))
print("{n}今年{a}岁".format(n="haha", a=19))
# pi 圆周率
import math
print("{0:.2f}".format(math.pi))
print(f"{math.pi:.4f}")

# 格式化控制标记符
n=42
print(f"{n:>6}") #打印占 6 位宽、右对齐
print(f"{n:*<6}") #打印占 6 位宽、左对齐,*填充

#打印百分比
x=7
print(f"{x:.1%}")

# 类型转换
s="123"
print(int(s)+1)
num=456
print(str(num)+"abc")
f="3.14"
print(float(f)*2)
n=65
print(chr(n))
c="A"
print(ord(c))
#print("abc"+123) 
#abc是字符串类型，123是整数类型，不能直接拼接
print("abc"+str(123))