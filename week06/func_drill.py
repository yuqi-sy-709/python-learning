def fact(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s
print(fact(6))

def fact_2(n,m=2):
    s=1
    for i in range(1,n+1):
        s*=i
    return s//m,s,m
print(fact_2(3,5))
 
def fact_3(n,*b):
    s=1
    for i in range(1,n+1):
        s*=i
    for item in b:
        s*=item
    return s
print(fact_3(5,2,3))

ls=['f','F']
def func(a):
    ls.append(a)
    return 
func('Q')
print(ls)

f=lambda x,y: x+y
print(f(1,2))

