#=====P4414 [COCI 2006/2007 #2] ABC======
x, y, z = map(int, input().split())
a, b, c = input() 
if x > y: x, y = y, x
if x > z: x, z = z, x
if y > z: y, z = z, y
if a == 'A': num1 = x
elif a == 'B': num1 = y
else: num1 = z
if b == 'A': num2 = x
elif b == 'B': num2 = y
else: num2 = z
if c == 'A': num3 = x
elif c == 'B': num3 = y
else: num3 = z

print(num1, num2, num3)



#==============三位数排序==================
x,y,z = map(int,input().split())
if x>y:
    x,y = y,x
if x>z:
    x,z = z,x
if y>z:
    y,z = z,y
print(x,y,z)

