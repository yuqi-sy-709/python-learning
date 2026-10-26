# prelearn_mini1.py 
# Mini-1 预学块｜9 个核心函数最小可运行例子 
# 验收标准：每个函数 1 个自写例子，跑通，commit → 11.1 复盘不查资料默写调用形式 

from pathlib import Path # 路径处理核心库 
import shutil            # 文件移动/复制 
import datetime          # 时间戳转人类可读时间 
import os                # 备用（周六 os.walk 再细讲）

# 测试目录：放在当前 week07/ 下的 test_mini1 子目录，避免污染 Mini-1 正式代码
TEST_DIR=Path(__file__).parent/'test_mini1'

# 每次跑都确保测试文件存在
TEST_DIR.mkdir(parents=True,exist_ok=True)
(TEST_DIR / 'temp.txt' ).write_text( 'mini1 预学测试' , encoding= 'utf-8' )
(TEST_DIR / 'temp.JPG' ).write_text( 'JPG 后缀测试' , encoding= 'utf-8' )
(TEST_DIR / 'no_suffix' ).write_text( '无后缀测试' , encoding= 'utf-8' ) 
print ( "✅ 测试目录与文件已创建" )


# ======================================== 
# 函数名：Path 
# 参数：str 类型的路径（不传 = 当前目录） 
# 返回值：pathlib.Path 对象（把字符串路径转成可操作的对象） 
# ======================================== 
# 最小例子
p_current=Path(__file__).parent #当前目录
p_relative=Path('test_mini1/temp.txt')  #相对路径
print(f'当前目录绝对路径：{p_current.resolve()}')
print(f"测试文件相对路径：{p_relative}")

# 变形练习：用Path 造一个绝对路径
p_abs=Path(r"D:/学习/学习手册-Trae版/.trae/python-learning/week07/")
print(f"绝对路径：{p_abs.resolve()}")

#======================================== 
# 函数名：Path.iterdir 
#参数：无 
# 返回值：迭代器（for 循环遍历，每个子项都是 Path 对象） 
# 注意：不递归，只看当前目录第一层 
# ======================================== 
# 最小例子
print("\n--- 遍历 test_mini1 直接子项 ---")
for item in TEST_DIR.iterdir():
    print(item.name)

# 变形练习：用 iterdir()+is_file(),只打印文件，不打印子目录
print("\n--- 只打印文件---")
for item in TEST_DIR.iterdir():
    if item.is_file():
        print(item.name)

# ======================================== 
# 函数名：Path.rglob 
# 参数：pattern（字符串，比如 '*' = 所有，'*.py' = 所有 .py 文件） 
# 返回值：迭代器（递归遍历，包括所有子目录里的文件） 
# ======================================== 
# 最小例子
print("\n--- 递归找 test_mini1 所有子项 ---")
for f in TEST_DIR.rglob('*'):
    print(f)

# 变形练习：只打印 week07 目录下的所有 .py 文件的完整路径
print("\n--- 只打印完整路径---")
week07_dir=p_current
for f in week07_dir.rglob('*.py'):
    print(f.resolve())

# ======================================== 
# 函数名：Path.is_file 
# 参数：无 
# 返回值：bool（True = 文件，False = 子目录 / 不存在） 
# ======================================== 
# 最小例子
f=TEST_DIR / 'temp.txt' 
print ( f"\n {f.name} 是文件吗？ {f.is_file()} " ) # True 
print ( f" {TEST_DIR} 是文件吗？ {TEST_DIR.is_file()} " ) # False（子目录）


# 变形练习：只打印 week07 目录下的所有 JPG 文件
print("\n--- 只打印 JPG 文件---")
for item in TEST_DIR.iterdir():
    if item.is_file() and item.suffix.lower()=='.jpg':
        print(item.name)

# ======================================== 
# 函数名：Path.suffix 
# 参数：无 
# 返回值：str（带点的后缀，比如 '.txt'；无后缀返回 ''）
# 函数名：str.lower 
# 参数：无 
# 返回值：str（转小写） 
# ======================================== 
# 最小例子 
f1=TEST_DIR / 'temp.txt' 
f2=TEST_DIR / 'temp.JPG' 
f3=TEST_DIR / 'no_suffix'
print ( f"\n {f1.name} 后缀： {f1.suffix.lower()} " ) # .txt
print ( f" {f2.name} 后缀： {f2.suffix.lower()} " ) # .jpg（大写转小写）
print ( f" {f3.name} 后缀：' {f3.suffix.lower()}' " ) # ''(空字符串)

# 变形练习：自建。PY 后缀文件，打印suffix.lower()
f4=TEST_DIR/'temp.PY'
print(f"\n{f4.name} 后缀 {f4.suffix.lower()}")
# ======================================== 
# 函数名：Path.stat 
# 参数：无 
# 返回值：os.stat_result 对象（包含文件元信息：大小、修改时间戳等） 
# 其中 st_mtime = 最后修改的时间戳（浮点数，秒） 
# 函数名：datetime.datetime.fromtimestamp 
# 参数：timestamp（浮点数，秒） 
# 返回值：datetime.datetime 对象（人类可读的日期时间） 
# ======================================== 
# 最小例子
f=TEST_DIR/'temp.txt'
mtime_ts=f.stat().st_mtime    # 取时间戳
mtime_dt=datetime.datetime.fromtimestamp(mtime_ts)  #转 datetime
print(f"\n{f.name} 修改时间戳：{mtime_ts:.0f}秒")
print(f"\n{f.name} 修改时间：{mtime_dt}")

# 变形练习：用datetime.strftime把datetime 转成'YYYY-MM-DD HH:MM:SS'格式
f=TEST_DIR/'temp.txt'
mtime_ts=f.stat().st_mtime
mtime_dt=datetime.datetime.fromtimestamp(mtime_ts)  
print(f"\n{f.name} 修改时间：{mtime_dt.strftime('%Y-%m-%d %H:%M:%S')}")

# ======================================== 
# 函数名：shutil.move 
# 参数：src（源路径）、dst（目标路径），Path 或 str 均可（部分环境要求 str） 
# 返回值：dst（移动后的目标路径） 
# 注意：Windows 下保险起见套 str() 转换 
# ======================================== 
# 最小例子 
# 先造临时文件和目标目录
src = TEST_DIR / 'to_move.txt'
src.write_text('我要被移动啦', encoding='utf-8')
move_dir = TEST_DIR / 'moved'
move_dir.mkdir(parents=True, exist_ok=True)

# 移动（套 str() 保险）
dst = shutil.move(str(src), str(move_dir))
print(f"\n已第一次移动:{dst}")

# 变形练习：把moved/to_move.txt 再移回 test_mini1/ 目录
src2 = TEST_DIR / 'moved' / 'to_move.txt'
dst2=shutil.move(str(src2),str(TEST_DIR))
print(f"\n已第二次移动:{dst2}")

# ======================================== 
# 函数名：Path.mkdir 
# 参数： 
#   - parents（bool）：True = 自动创建中间目录（a/b/c 中 a 不存在也能创建） 
#   - exist_ok（bool）：True = 目录已存在不报错（可以多跑几次） 
# 返回值：无 
# ======================================== 
# 最小例子
new_dir = TEST_DIR / '预学练手目录' 
new_dir.mkdir(parents= True , exist_ok= True ) 
print ( f"\n目录 {new_dir} 创建成功： {new_dir.exists()} " )

# 变形练习：造一个嵌套目录test_mini1/a/b/c ,用mkdir(parents=True)一次创建
new_dir=TEST_DIR / 'a' / 'b' / 'c'
new_dir.mkdir(parents= True , exist_ok= True )
print(f'\n目录{new_dir} 创建成功：{new_dir.exists()}')