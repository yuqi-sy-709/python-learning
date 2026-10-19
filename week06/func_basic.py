# 定义
def fact(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s
print(fact(5))
# 可选参数
def fact_2(n,m=1):
    s=1
    for i in range(1,n+1):
        s*=i
    return s//m
print(fact_2(5,2))
# 可变参数
def fact_3(n,*b):
    s=1
    for i in range(1,n+1):
        s*=i
    for item in b:
        s*=item
    return s
print(fact_3(5,2,3))
# 局部变量为组合数据类型
ls=['F','f']
def func(a):
    ls.append(a)
    return
func('C')
print(ls)

# lambda函数
f=lambda x,y:x+y
print(f(1,2))