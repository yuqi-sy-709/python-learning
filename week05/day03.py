# P1035 级数求和 （n)
k=int(input())
s=0
n=0
while s<=k:
    n+=1
    s+=1/n
print(n)

# P5721 数字直角三角形 (n²)
n=int(input())
num=1
for i in range(n):
    for _ in range(n-i):
        print(f"{num:02d}",end="")
        num+=1
    print()
