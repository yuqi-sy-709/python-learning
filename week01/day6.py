n=int(input())
t=0
for i in range(n):
    a=int(input())
    t+=a
avg=t/n
print("{0:.2f}".format(avg))
#==========================================
m,k=map(int,input().split())
c=str(m).count('3')
if c==k:
    print("YES")
else:
    print("NO")
