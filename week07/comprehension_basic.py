# 列表推导式
print([x*2 for x in range(5)])

print([x*2 for x in range(10) if x%2==0])

print(['偶' if x%2==0 else '奇' for x in range(5)])

# 嵌套循环
print([(i,j) for i in range(3) for j in range(3)])

#字典推导式
print({x:x**2 for x in range(5)})

print({k:v*2 for k,v in {'a':1,'b':2}.items()})

# 集合推导式
print({x%3 for x in range(10)})

# 变形：

# 1.词长字典
print({w:len(w) for w in "the quick brown fox jumps over".split()})

# 2.矩阵转置
m=[[1,2,3],[4,5,6]]
print([[row[i] for row in m] for i in range(3)])

