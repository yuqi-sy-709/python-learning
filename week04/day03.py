# P1914 凯撒密码
n=int(input())
s=input()
ans=""
for c in s:
    x=ord(c)
    m=(x-97+n)%26
    ans=ans+chr(m+97)
print(ans)

# P5733 自动修正
s=input()
print(s.upper())

# P1200 你的飞碟在这儿
x = input()
y = input()
n, k = 1, 1
for c in y:
    n = (n * (ord(c) - 64)) % 47
for b in x:
    k = (k * (ord(b) - 64)) % 47
if k == n:
    print("GO")
else:
    print("STAY")