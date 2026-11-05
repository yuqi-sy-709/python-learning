import json
from pathlib import Path

path=Path(__file__).parent/"scores.json"

data=[
    {"name":"张三","score":85,"班级":"一班"},
    {"name":"李四","score":92,"班级":"二班"}
]

with open(path,"w",encoding="utf-8")as f:
    json.dump(data,f,ensure_ascii=False,indent=2)

print("写好了：",path)

# === 读：json.load 直接还原成原类型 ===
with open(path,"r",encoding="utf-8")as f:
    loaded=json.load(f)
print("类型：",type(loaded))
print("第一条的分数类型：",type(loaded[0]["score"]))
print("平均分：",sum([s["score"] for s in loaded])/len(loaded))

