import json
from pathlib import Path

scores_path = Path(__file__).parent / "scores.json"

if scores_path.exists():
    with open(scores_path, "r", encoding="utf-8") as f:
        students = json.load(f)
else:
    students = []

def add_student():
    name=input("请输入姓名：")
    score=int(input("请输入成绩："))
    students.append({'name':name,'score':score})
    print(f"{name} {score} 已添加")

def delete_student():
    name=input("请输入要删除的名字：")
    for i,s in enumerate(students):
        if s['name']==name:
            students.pop(i)
            print(f"{name} 已删除")
            return 
        print(f"{name} 未找到")

def update_score():
    name=input("请输入要修改的名字：")
    for s in students:
        if s['name']==name:
            new_score=int(input("请输入新的成绩："))
            s['score']=new_score
            print(f"{name} 已修改为 {new_score}")
            return 
        print(f"{name} 未找到")

def query():
    name=input("请输入要查询的姓名（回车查全部):")
    if name=='':
        for s in students:
            print(f"{s['name']} {s['score']}")
        return 
    for s in students:
        if s['name']==name:
            print(f"{name} {s['score']}")
            return 
        print(f"{name} 未找到")

def sort_by_score():
    sorted_list=sorted(students,key=lambda s:s['score'],reverse=True)
    for s in sorted_list:
        print(f"{s['name']} {s['score']}")

def statistics():
    if not students:
        print("暂无学生信息")
        return 
    scores=[s['score'] for s in students]
    print(f"人数：{len(students)}")
    print(f"平均分：{sum(scores)/len(scores):.1f}")
    print(f"最高分：{max(scores)}")
    print(f"最低分：{min(scores)}")

def main():
    while True:
        print ( "\n===== 成绩管理系统 =====" ) 
        print ( "1. 添加" ) 
        print ( "2. 删除" ) 
        print ( "3. 修改分数" ) 
        print ( "4. 查询" ) 
        print ( "5. 按分数排序" ) 
        print ( "6. 统计" ) 
        print ( "0. 退出" )
        choice = input ( "选择功能：" ) 
        
        if choice == "1" : 
            add_student() 
        elif choice == "2" : 
            delete_student() 
        elif choice == "3" : 
            update_score() 
        elif choice == "4" :
            query() 
        elif choice == "5" :  
            sort_by_score() 
        elif choice == "6" : 
            statistics() 
        elif choice == "0" : 
            print ( "再见" ) 
            with open(scores_path, "w", encoding="utf-8") as f:
                json.dump(students, f, ensure_ascii=False, indent=2)
            break 
        else : 
            print ( "无效选择" )

main()