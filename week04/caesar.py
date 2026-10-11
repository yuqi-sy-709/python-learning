mode=input("加密(e) 还是解密(d)？")
t=input("要处理的文字：")
n=int(input("移动几位："))
ans=""
for c in t:
    if 'a'<=c<='z':
        if mode=="e":
            m=(ord(c)-97+n)%26
        else:
            m=(ord(c)-97-n)%26
        ans=ans+chr(m+97)
    else:
        ans=ans+c
print(ans)