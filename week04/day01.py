s="PythonLanguage"
# 打印第一个字符，最后一个字符
print(s[0])
print(s[-1])

# 打印s[3]和s[-4]的字符，结果为h和u
print(s[3],s[-4])

# 切出`"Python"` 和`"Language"`
print(s[0:6])
print(s[6:])

#用步长 2 取所有偶数位字符
# 把整个字符串倒序（一步，用切片）
#取`s[2:8]` ，结果为thonLa
print(s[0::2])
print(s[::-1])
print(s[2:8])

#s + "2026"` 拼起来打印
print(s+"2026")

# “py”*3                                                                                                                                                                                         
print("py"*3)

# 检查`s`是否包含`"Lang"`"java"
if "Lang" in s:
    print("True")
else:
    print("False")
if "java" in s:
    print("True")
else:
    print("False")
#全大写、全小写各打印一次

# 全大写，全小写
#`len(s)` 打印
#数出字母`a` 在 s 里出现几次
# 把`"Python"` 替换成`"Java"` 
# 再单独 print 一次原 s，观察 原字符串变没变 
#用`"-".join(...)` 把 s 每个字符之间插上横杠打印
print(s.upper())
print(s.lower())
print(len(s))
print(s.count("a"))
print(s.replace("Python","Java"),s)
print("-".join(s))



