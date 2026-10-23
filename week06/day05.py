# P5735 闰年展示
x,y=map(int,input().split())
res=[]
for i in range(x,y+1):
    if (i%4==0 and i%100!=0) or (i%400==0):
        res.append(i)
print(len(res))
print(' '.join(map(str,res)))

# P5734 文字处理软件
import sys
q = int(sys.stdin.readline())
text = sys.stdin.readline().strip()
for _ in range(q):
    ops = sys.stdin.readline().split()
    cmd = ops[0]
    if cmd == '1':
        text = text + ops[1]
        sys.stdout.write(text + '\n')
    elif cmd == '2':
        a, b = int(ops[1]), int(ops[2])
        text = text[a:a+b]
        sys.stdout.write(text + '\n')
    elif cmd == '3':
        a = int(ops[1])
        text = text[:a] + ops[2] + text[a:]
        sys.stdout.write(text + '\n')
    elif cmd == '4':
        pos = text.find(ops[1])
        sys.stdout.write(str(pos) + '\n')