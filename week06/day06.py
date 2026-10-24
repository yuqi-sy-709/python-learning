# P5743 猴子吃桃
n=int(input())
def p(n):
    x=1
    for i in range(n-1):
        x=(x+1)*2
    return x
print(p(n))

# fact(n) 递归版
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(8))

# fact(n) 循环版
def fact_2(n):
    s=1
    for i in  range(1,n+1):
        s*=i
    return s
print(fact_2(6))

# 斐波那契第n项 递归版
def fib(n):
    if n==1 or n==2:
        return 1
    elif n==0:
        return 0
    else:
        return fib(n-1)+fib(n-2)
print(fib(19))

# 素数判断
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
print(is_prime(13))

# 辗转相除求最大公约数
def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a
print("GCD：", gcd(12,8), gcd(6,12), gcd(10,5))




