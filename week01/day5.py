h=list(map(int,input().split()))
m=int(input())+30
n=0
for x in h:
    if x<=m:
        n+=1
print(n)
#==========================================
a,b,c=map(int,input().split())
if a+b>c and a+c>b and c+b>a:
    print("1")
else:
    print("0")
#==========================================
x=float(input())
if 0<=x<5:
    y=-x+2.5
elif 5<=x<10:
    y=2-1.5*(x-3)*(x-3)
elif 10<=x<20:
    y=x/2-1.5
print(f"{y:.3f}")