import csv
from pathlib import Path

path = Path(__file__).parent / "scores.csv"

rows = [
    ["姓名", "分数"],
    ["张三", 85],
    ["李四", 92],
]

# newline='' 必须加：不加的话，Windows 下每行末尾会多一个空行
with open(path, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    for r in rows:
        writer.writerow(r)     

print("写好了：", path)

# === 读：csv.reader 逐行读出，每行是一个列表 ===
with open(path, "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# === DictReader：第一行变表头，每行是一个字典 ===
with open(path, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)                          # {'姓名': '张三', '分数': '85'}
        print(row["姓名"], int(row["分数"])) # 分数要 int() 转，因为读回来是字符串

total=0
count=0
with open(path,'r',encoding="utf-8",newline="")as f:
    reader=csv.DictReader(f)
    for row in reader:
        total+=int(row["分数"])
        count+=1
print(f"平均分：{total/count:.1f}")