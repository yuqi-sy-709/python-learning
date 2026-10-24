c=4                 
s=0                    
d=[None]*c

def append(x):
    global c,s,d
    if s==c:
        n_d=[None]*(c*2)
        for i in range(s):
            n_d[i]=d[i]
        d=n_d
        c=c*2
        print(f"扩容{s}→{c}")
    d[s]=x
    s=s+1

def pop():
    global c,s,d
    s-=1
    f=d[s]
    d[s]=None
    return f

def insert(i,x):
    global c,s ,d
    if i<0 or i>s:
        raise IndexError("下标越界")
    if s==c:
        n_d=[None]*(c*2)
        for j in range(s):
            n_d[j]=d[j]
        d=n_d
        c*=2
        print(f"扩容{s}→{c}")
    for l in range(s,i,-1):
        d[l]=d[l-1]
    d[i]=x
    s=s+1

def index(x):
    global c,s,d
    for i in range(s):
        if d[i]==x:
            return i
    return -1

for k in [10, 20, 30, 40, 50]:
    append(k)
    print(f"装入{k} 容量{c} 已用{s}")

print("pop:", pop())
insert(1, 99)
print([d[i] for i in range(s)])
print("index(30):", index(30))
print("index(999):", index(999))
