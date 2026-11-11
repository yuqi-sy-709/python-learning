import json


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def introduce(self):
        print(f"我是{self.name}，我有{self.score}分")


class Manager:
    def __init__(self):
        self.students = []

    def add(self, student):
        self.students.append(student)

    def query(self, name):
        for s in self.students:
            if s.name == name:
                return s
        return None

    def delete(self, name):
        for i, s in enumerate(self.students):
            if s.name == name:
                self.students.pop(i)
                return True
        return False

    def update_score(self, name, new_score):
        stu = self.query(name)
        if stu is not None:
            stu.score = new_score
            return True
        return False

    def sort_by_score(self):
        sorted_list = sorted(self.students, key=lambda s: s.score, reverse=True)
        for s in sorted_list:
            s.introduce()

    def statistics(self):
        if not self.students:
            print("暂无学生信息")
            return
        scores = [s.score for s in self.students]
        print(f"人数：{len(scores)}")
        print(f"平均分：{sum(scores)/len(scores):.1f}")
        print(f"最高分：{max(scores)}")
        print(f"最低分：{min(scores)}")

    def save(self, path):
        data = [{'name': s.name, 'score': s.score} for s in self.students]
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    @classmethod
    def load(cls, path):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        mgr = cls()
        for d in data:
            mgr.add(Student(d['name'], d['score']))
        return mgr

def main():
    scores_path = "scores.json"
    if __import__('pathlib').Path(scores_path).exists():
        mgr = Manager.load(scores_path)
    else:
        mgr = Manager()
    while True:
        print("\n===== 成绩管理系统 =====")
        print("1. 添加")
        print("2. 删除")
        print("3. 修改分数")
        print("4. 查询")
        print("5. 按分数排序")
        print("6. 统计")
        print("0. 退出")
        choice = input("选择功能：")

        if choice == "1":
            name = input("请输入姓名：")
            score = int(input("请输入成绩："))
            mgr.add(Student(name, score))
            print(f"{name} {score} 已添加")
        elif choice == "2":
            name = input("请输入要删除的名字：")
            ok = mgr.delete(name)
            if ok:
                print(f"{name} 已删除")
            else:
                print(f"{name} 未找到")
        elif choice == "3":
            name = input("请输入要修改的名字：")
            new_score = int(input("请输入新成绩："))
            ok = mgr.update_score(name, new_score)
            if ok:
                print(f"{name} 已修改为 {new_score}")
            else:
                print(f"{name} 未找到")
        elif choice == "4":
            name = input("请输入要查询的姓名（回车查全部）：")
            if name == '':
                for s in mgr.students:
                    s.introduce()
            else:
                stu = mgr.query(name)
                if stu is not None:
                    stu.introduce()
                else:
                    print(f"{name} 未找到")
        elif choice == "5":
            mgr.sort_by_score()
        elif choice == "6":
            mgr.statistics()
        elif choice == "0":
            print("再见")
            mgr.save("scores.json")
            break
        else:
            print("无效选择")

if __name__ == '__main__':
    main()