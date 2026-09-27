#===阶乘函数===
def fact(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s

#===找最小值===
n=int(input())
a=list(map(int,input().split()))
min_a=a[0]
for i in range(n):
    if a[i]<min_a:
        min_a=a[i]
print(min_a)

#===猜数字===
n=42
while True:
    guess=int(input("请输入你猜的数字："))
    if guess==n:
        print("猜对了！")
        break
    elif guess<n:
        print("小了")
    else:
        print("大了")

