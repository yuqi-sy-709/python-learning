s1=set()
s2={1,2,3}
s3=set("abc")
s4=set([1,2,2,3,3,3])
print(type(s1),type({}))

# 查
print(3 in s2)
print(99 in s2)

# 增
s2.add(4)
s2.update([5,6])
#s2.add([1,2])

# 删
s={1,2,3}
s.remove(3)
#s.remove(99)
s.discard(2)
s.pop()
print(s)

# 集合运算
a={1,2,3,4}
b={3,4,5}
print(a|b)
print(a&b)
print(a-b)
print(b-a)
print(a^b)
print(a.difference(b),a.union(b),a.intersection(b))

# 去重
l=[1,2,2,3,3,3]
print(list(set(l)))

# 遍历
for x in s2:
    print(x)

# 不可变集合
fs = frozenset([1, 2, 3])
#fs.add(4)                        # ← 抛 AttributeError，验完注释掉
d = {frozenset([1, 2]): 'hello'} # frozenset 能当字典的键
print(d)
#d2 = {set([1, 2]): 'x'}          # ← 抛 TypeError: unhashable type: 'set'

# 变形
# 1.去重且保序
s=[3,1,2,1,3,4,2]
res=list(dict.fromkeys(s))
print(res)

s=[3,1,2,1,3,4,2]
seen=set()
r=[]
for item in s:
    if item not in seen:
        r.append(item)
        seen.add(item)
print(r)
# 2.两个句子的字符比较
a="hello world"
b="python hello"
sa=set(a)
sb=set(b)
print("共有字符：",sa&sb)
print("只在一方出现的字符: ",sa^sb)
#想要排除空格，则在第一步后面加.replace(" ","")


