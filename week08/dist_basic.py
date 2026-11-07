head={'data':None,'prev':None,'next':None}
size=0

def insert_head(x):
    global head,size
    new_node={'data':x,'prev':head,'next':head['next']}
    if head['next']!=None:
        head['next']['prev']=new_node
    head['next']=new_node
    size+=1

def insert_tail(x):
    global head,size
    new_node={'data':x,'prev':None,'next':None}
    p=head
    while p['next']!=None:
        p=p['next']
    new_node['prev']=p
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
    if del_node['next']!=None:
        del_node['next']['prev']=p
    size-=1
    return del_node['data']

def pop_tail():
    global head,size
    if size==0:
        raise IndexError("链表为空")
    pop(size-1)

def pop_left():
    global head,size
    if size==0:
        raise IndexError("链表为空")
    first=head['next']
    head['next']=first['next']
    if first != None:
        head['next']['prev']=head
    size-=1
    return first['data']
def pop_right():
    global head,size
    if size==0:
        raise IndexError("链表为空")
    last=head['next']
    while last['next']!=None:
        last=last['next']
    last['prev']['next']=None
    size-=1
    return last['data']

def print_forward():
    p=head['next']
    res=[]
    while p!=None:
        res.append(str(p['data']))
        p=p['next']
    print("->".join(res))

def print_backward():
    p = head
    while p['next'] != None:       
        p = p['next']
    res = []
    while p != head:              
        res.append(str(p['data']))
        p = p['prev']
    print(" → ".join(res))

if __name__=='__main__':
    head['next']=None;size=0
    insert_tail(10)
    insert_tail(20)
    insert_tail(30)
    print_forward()
    pop_left()
    print_forward()
    pop_right()
    print_forward()
    print_backward()