class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.is_empty():
            raise IndexError("空栈不能出")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("空栈没有栈顶")
        return self.items[-1]

        
class LinkedStack:
    def __init__(self):
        #self.items = []          # len(self.items)=size
        self.head={'data':None,'next':None}
    
    def is_empty(self):
        #return self.items == []
       return self.head['next'] is None
    
    def push(self, x):
        #self.items.append(x)     # 列表尾部 = 栈顶，append 刚好是 O(1)
        new_node={'data':x,'next':self.head['next']}
        self.head['next']=new_node
    
    def pop(self):              # 拿走并返回
        #if self.is_empty():
            #raise IndexError("空栈不能出")
        #return self.items.pop()  # 列表尾部 pop = O(1)，注意是 pop() 不带参数（带参数是按下标删）
        if self.is_empty():
           raise IndexError("空栈不能出")
        first=self.head['next']
        self.head['next']=first['next']
        return first['data']
    
    def peek(self):             # peek只返回不拿走
        #if self.is_empty():
            #raise IndexError("空栈没有栈顶")
        #return self.items[-1]    # 倒数第一个元素，不删除，只返回
        if self.is_empty():
            raise IndexError("空栈没有栈顶")
        return self.head['next']['data']

if __name__ == '__main__':
    print("--- 链栈测试 ---")
    s2 = LinkedStack()
    s2.push(10)
    s2.push(20)
    s2.push(30)
    print(s2.peek())
    print(s2.pop())
    print(s2.pop())
    print(s2.is_empty())
    print(s2.pop())
    print(s2.is_empty())
