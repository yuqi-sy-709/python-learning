#===for循环：打印1-10的数字===
for i in range(1,11):
    print(i)

#===while循环：猜数字游戏===
n=42
while True:
    guess=int(input("请输入你猜的数字："))
    if guess>n:
        print("大了")
    elif guess<n:
        print("小了")
    else:
        print("猜对了")
        break

#===for+if:打印1-100中所有3的倍数===
for i in range(1,101):
    if i%3==0:
        print(i)