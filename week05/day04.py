# P5709 Apples Prologue / 苹果和虫子
m,t,s=map(int,input().split())
if t==0:
    print(0)
else:
    if s % t == 0:
        eat = s // t
    else:
        eat = s // t + 1
    l=m-eat
    if l<0:
        l=0
    print(l)
# P5722 数列求和
n=int(input())
num=0
for i in range(1,n+1):
    num+=i
print(num)

# P5736 质数筛
n=int(input())                   
nums=list(map(int,input().split()))  
for x in nums:                     
    if x<2:
        continue                   
    is_prime=True                 
    for i in range(2,int(x**0.5)+1):  
        if x%i==0:              
            is_prime=False        
            break                   
    if is_prime:
        print(x, end=" ")

