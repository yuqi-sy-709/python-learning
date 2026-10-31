head = {'data': None, 'next': None}
size=0
def append(x):
    global head,size
    new_node={'data':x,'next':None}
    p=head
    while p['next']!=None:
        p=p['next']
    p['next']=new_node
    size+=1

def get(i):
    global head,size
    if i<0 or i>=size:
        raise IndexError("下标越界")
    p=head['next']
    for _ in range(i):
        p=p['next']
    return p['data']

def insert(i,x):
    global head,size
    if i<0 or i>size:
        raise IndexError("下标越界")
    new_node={'data':x,'next':None}
    p=head
    for _ in range(i):
        p=p['next']
    new_node['next']=p['next']
    p['next']=new_node
    size+=1

def pop(i):
    global head,size
    if i<0 or i>=size:
        raise IndexError("下标越界")
    p=head
    for _ in range(i):
        p=p['next']
    del_node=p['next']
    p['next']=del_node['next']
    size-=1
    return del_node['data']

def index(x):
    global head,size
    p=head['next']
    idx=0
    while p!=None:
        if p['data']==x:
            return idx
        p=p['next']
        idx+=1
    return -1

def print_list():
    global head
    res=[]
    p=head['next']
    while p!=None:
        res.append(str(p['data']))
        p=p['next']
    print(" ".join(res))

def reverse():
    global head
    prev=None
    curr=head['next']
    while curr!=None:
        nxt=curr['next'] 
        curr['next']=prev
        prev=curr
        curr=nxt
    head['next']=prev

def find_mid():
    global head
    slow=head['next']
    if slow==None:
        return None
    fast=head['next']
    while fast != None and fast['next'] != None:
        slow=slow['next']
        fast=fast['next']['next']
    return slow['data']

def has_cycle():
    global head
    slow=head['next']
    fast=head['next']
    while fast != None and fast['next'] != None:
        slow=slow['next']
        fast=fast['next']['next']
        if slow is fast:
            return True
    return False


if __name__ == '__main__':
    append(10); append(20); append(30);append(40)
    p=head['next']
    while p['next']!=None:
        p=p['next']
    p['next']=head['next']['next']
    #print_list()
    #print(get(0), get(1), get(2))
    #insert(1, 99); print_list()
    #reverse(); print_list()
    #print(find_mid())
    print(has_cycle())
    p['next']=None
    print_list()
    head['next'] = None; size = 0        # 清空链表（head 的下一个指向 None，就是空表了）
    append(10)                           # 链表变成 [10]
    head['next']['next'] = head['next']  # 节点 10 的 next 指向它自己 → 自环
    print(has_cycle())                   # 期望 True
    head['next']['next'] = None          # 拆掉自环，恢复成正常的 [10]
