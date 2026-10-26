# 第1题 创建列表
ls1 = [1, 2, 3]
ls2 = list('abc')
ls3 = []
print("1 创建列表：")
print(f"ls1 = {ls1}")
print(f"ls2 = {ls2}")
print(f"ls3 = {ls3}\n")

# 第2题 索引（用ls1 = [1,2,3]测试）
print("2 索引：")
print(f"ls1[0] = {ls1[0]}")   # 正索引，第0个元素
print(f"ls1[-1] = {ls1[-1]}") # 负索引，最后一个元素
print()

# 第3题 切片
ls = [0,1,2,3,4]
print("3 切片，测试列表 ls = [0,1,2,3,4]")
print(f"ls[1:3] = {ls[1:3]}")
print(f"ls[:2] = {ls[:2]}")
print(f"ls[::2] = {ls[::2]}")
print(f"ls[::-1] = {ls[::-1]}")
print()

# 变形：取第2、4、6个元素
nums = [1, 2, 3, 4, 5, 6]
print(f"nums[::2] = {nums[::2]}")

# 第4题 增：append / insert / extend
ls4 = [10,20]
print("4 增加元素，初始 ls4 = [10,20]")
ls4.append(30)
print(f"append(30) → {ls4}")

ls4.insert(1, 99)
print(f"insert(1,99) → {ls4}")

ls4.extend([4,5])
print(f"extend([4,5]) → {ls4}\n")

# 第5题 删：pop / remove / del
ls5 = [1,2,3,4,5]
print("5 删除，初始 ls5 = [1,2,3,4,5]")
val1 = ls5.pop()
print(f"pop() 删除最后一个元素，删掉的值{val1}, ls5={ls5}")

val2 = ls5.pop(0)
print(f"pop(0) 删除索引0元素,删掉的值{val2}, ls5={ls5}")

ls5.remove(3)
print(f"remove(3) 删除值为3的元素, ls5={ls5}")

del ls5[0]
print(f"del ls5[0] 删除索引0, ls5={ls5}\n")

# 第6题 改
ls6 = [1,2,3,4]
print("6 修改，初始 ls6 = [1,2,3,4]")
ls6[0] = 99
print(f"ls6[0]=99 → {ls6}")

ls6[1:3] = [7,8,9]
print(f"ls6[1:3]=[7,8,9] → {ls6}\n")

# 第7题 查
ls7 = [10,20,30,40]
print("7 查询,ls7 = [10,20,30,40]")
print(f"len(ls7) = {len(ls7)}")
print(f"max(ls7) = {max(ls7)}")
print(f"min(ls7) = {min(ls7)}")
print(f"sum(ls7) = {sum(ls7)}")
print(f"20 in ls7 → {20 in ls7}")
print(f"ls7.index(30) → {ls7.index(30)}\n")

# 第8题 排序、反转
ls8 = [3,1,4,2]
print("8 排序反转，初始 ls8 = [3,1,4,2]")
ls8.sort()
print(f"sort()升序 → {ls8}")
a = ls8.sort()
print(a)      # 预期：None

ls8.sort(reverse=True)
print(f"sort(reverse=True)降序 → {ls8}")

raw = [3, 1, 4, 2]
print(sorted(raw, reverse=True))  # 预期 [4, 3, 2, 1]
print(raw)                        # 预期 [3, 1, 4, 2] 不变

ls8.reverse()
print(f"reverse()原地反转 → {ls8}")

# 坑2 赋值不是复制
x = [1, 2]
y = x
y.append(99)
print(x)      # 预期 [1, 2, 99]

z = x[:]      # 切片才是复制
z.append(100)
print(x)      # 预期 [1, 2, 99] 不变