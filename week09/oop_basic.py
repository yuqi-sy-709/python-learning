class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score

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

    def update(self,name,score):
        stu=self.query(name)
        if stu is not None:
            stu.score=score
            return True
        return False

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