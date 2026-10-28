d1={}
d2=dict()
d3=dict(a=1,b=2)
d4={'a':1, 'b':2, 'c':3}

# 查
print(d1.get('a',9))
print(d4['a'])

# 改
d4['a']=4
print(d4)

# 删
del d4['a']
x=d4.pop('b')
print(d4,x)

# 遍历
for key in d4:
    print(key, d4[key])
for k,v in d4.items():   
    print(k,v)
print(d4.keys())
print(d4.values())

# in ，只认键，不认值
print("x" in d4)
print("a" in d4)
print(4 in d4)

# update 合并字典
d1.update(d4)
print(d1)

# setdefault vs get：唯一区别是它会真的写进字典
print(d2.setdefault('a',9))
print(d2)

# 变形练习：
# 1. 统计字符串中每个字符出现的次数
d=['a','b','a','c','b','a']
count={}
for ch in d:
    if ch in count:
        count[ch]+=1
    else:
        count[ch]=1
print(count)

# 2. 合并两个字典
d1 = {"a": 1, "b": 2}
d2 = {"b": 99, "c": 3, "d": 4}
for k, v in d2.items():
    if k in d1:
        d1[k] += v
    else:
        d1[k] = v
print(d1)