# 递归 阶乘
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

# 递归 字符串反转
def rvs(s):
    if s=='':
        return s
    else:
        return rvs(s[1:])+s[0]

# 阶乘 迭代版
def fact_iter(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s

# 递归 汉诺塔
count=0
def hanoi(n,src,dst,mid):
    global count
    if n==1:
        print("{}:{}→{}".format(n,src,dst))
        count+=1
    else:
        hanoi(n-1,src,mid,dst)
        print("{}:{}→{}".format(n,src,dst))
        count+=1
        hanoi(n-1,mid,dst,src)

print("递归版：", fact(0), fact(1), fact(5))
print("迭代版：", fact_iter(0), fact_iter(1), fact_iter(5))
hanoi(3, 'A', 'B', 'C')
print("总步数：", count)