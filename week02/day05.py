#===for循环：求n个整数的最小值===
n=int(input())
a=list(map(int,input().split()))
min_a=a[0]
for i in range(n):
    if a[i]<min_a:
        min_a=a[i]
print(min_a)

#===for循环：求n个整数的平均值===
n,k=map(int,input().split())
sumA=0
cntA=0
sumB=0
cntB=0
for i in range(1,n+1):
    if i%k==0:
        sumA+=i
        cntA+=1
    else:
        sumB+=i
        cntB+=1
avgA=sumA/cntA
avgB=sumB/cntB
print(f"{avgA:.1f} {avgB:.1f}")
        
#===一尺之棰===
n=int(input())
d=0
while n>1:
    n=n//2
    d+=1
print(d+1)  
    