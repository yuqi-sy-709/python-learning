#===================字符串切片=================
s="hello world"
print(s[0:5])
print(s[5:])
print(s[::-1])

#==============格式化输出：姓名和年龄============
n = input("请输入名字：")
y = int(input("请输入年龄："))
print("我叫{},今年{:.2f}岁".format(n, y))

#==============字符串操作======================
a=input("请输入一个字符串：")
print(a.upper())
print(a.lower())
print(a.replace("a","c"))
