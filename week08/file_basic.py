from pathlib import Path
# 读取文件内容
my_path = Path(__file__).parent / "file_basic.py"
with open(my_path, "r", encoding="utf-8") as f:
    content = f.read()
print("文件路径：", my_path)
print("前50字: ", content[:50])
print("总行数：", content.count("\n"))

# 写入文件
test_path=Path(__file__).parent / "test.txt"
with open(test_path, "w",encoding='utf-8') as f:
    f.write("这是第一行\n")
    f.write("这是第二行\n")

# 追加写入
with open(test_path,'a',encoding='utf-8') as f:
    f.write("这是追加的第三行\n")

# 验证：读一遍 test.txt 内容 ，确认追加的第三行是否正确
with open(test_path,'r',encoding='utf-8') as f:
    result=f.read()
print("==== test.txt 内容 ====")
print(result)