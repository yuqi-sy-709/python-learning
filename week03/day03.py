#===================小鱼航程=================
x,n=map(int,input().split())
y=0
for i in range(n):
    t=(x+i-1)%7+1
    if t<=5:
        y+=1
s=y*250
print(s)

#==================不高兴的津津===============
max=0
week=0
for day in range(1,8):
    a,b=map(int,input().split())
    total=a+b
    if total>max:
        max=total
        week=day
if max<=8:
        week=0
print(week)
        
        