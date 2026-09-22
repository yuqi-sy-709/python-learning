a,b=map(int,input().split())
print(a+b)
#=========================================
print(input().upper())
#=========================================
s = input()
if s[0] == '-':          
    s = s[1:]              
    print(-int(s[::-1]))   
else:
    print(int(s[::-1]))