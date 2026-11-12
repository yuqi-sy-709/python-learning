class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def introduce(self):
        print(f"我是{self.name}，我有{self.score}分")

    def __str__(self):
        return f"{self.name}({self.score}分)"

    def __eq__(self, other):
        return self.name == other.name and self.score == other.score

class HonStudent(Student):
    def __init__(self, name, score, scholarship):
        super().__init__(name, score)
        self.scholarship = scholarship

    def introduce(self):
        print(f"我是{self.name}，我有{self.score}分，奖学金{self.scholarship}元")

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

    def update(self,name,score):
        stu=self.query(name)
        if stu is not None:
            stu.score=score
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

mgr = Manager()
mgr.add(Student("张三", 85))
mgr.add(Student("李四", 92))
mgr.add(Student("王五", 78))

for s in mgr.students:
    s.introduce()

result = mgr.query("张三")
if result is not None:
    result.introduce()
else:
    print("没找到")

result2 = mgr.query("赵六")
print(result2)

ok = mgr.delete("李四")
print(ok)

ok2 = mgr.delete("赵六")
print(ok2)

ok = mgr.update("张三", 100)
print(ok)

ok2 = mgr.update("赵六", 60)
print(ok2)

for s in mgr.students:
    s.introduce()

mgr2 = Manager()
mgr2.add(Student("张三", 78))
mgr2.add(Student("李四", 95))
mgr2.add(Student("王五", 85))

mgr2.sort_by_score()

mgr2.statistics()

hon = HonStudent("小明", 98, 5000)
hon.introduce()
print(f"奖学金：{hon.scholarship}")
print(hon.name)
print(hon.score)

print(hon)
print(Student("张三", 85) == Student("张三", 85))