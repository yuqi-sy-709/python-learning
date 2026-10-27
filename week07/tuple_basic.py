# 1. 创建
t1=(1, 2, 3)
t2=tuple([4, 5, 6])       # tuple(可迭代对象)
t3=()                               # 空元组
print("创建：", t1, t2, t3)

# 2. ⚠️ 单元素陷阱
t_single_wrong=(1)          # 这是 int，不是 tuple！
t_single_ok=(1,)            # 必须加逗号
print(f"\n(1) 的类型是 {type(t_single_wrong).__name__},(1,) 的类型是 {type(t_single_ok).__name__}")

# 3. 索引 + 切片
t=(10, 20, 30, 40, 50)
print(f"\nt[0]={t[0]}, t[-1]={t[-1]}, t[1:3]={t[1:3]}, t[::-1]={t[::-1]}")

# 4. ⚠️ 不可变性：改元素直接报错
t_test=(1, 2, 3)
try:
    t_test[0] = 99           # 这行要抛 TypeError
except TypeError as e:
    print(f"\n不可变验证:{e}")

# 5. 连接 + 重复
t_a=(1, 2)
t_b=(3, 4)
print(f"\n(1,2)+(3,4)={t_a + t_b}")
print(f"(1,2)*3={t_a * 3}")

# 6. in / count / index
t_search=('a', 'b', 'a', 'c')
print(f"\n'a' in t_search = {'a' in t_search}")
print(f"t_search.count('a') = {t_search.count('a')}")
print(f"t_search.index('c') = {t_search.index('c')}")

# 7. list ↔ tuple 互转
my_list=[1, 2, 3]
my_tuple=tuple(my_list)       # list → tuple
back_list=list(my_tuple)      # tuple → list
print(f"\nlist→tuple: {my_tuple}, tuple→list: {back_list}")

# 8. 解包（新东西）
x, y, z=(10, 20, 30)
print(f"\n解包:x={x}, y={y}, z={z}")
a, *rest=(1, 2, 3, 4, 5)     # *rest 吃掉剩余所有
print(f"a={a}, rest={rest}")

# === 变形练习 ===
print("\n=== 变形 ===")
# ① 用切片反转元组
orig = (1, 2, 3, 4, 5)
reversed_tuple = orig[::-1]
print(f"反转：{orig} → {reversed_tuple}")

# ② list→tuple→改一个元素→转回list
work_list = [10, 20, 30]
work_tuple = tuple(work_list)
work_list_back = list(work_tuple)
work_list_back[0] = 99
print(f"原list={work_list}, tuple={work_tuple}, 改回list={work_list_back}")

