#==============apples=====================
x=int(input())
if x==0 or x==1:
    print(f"Today, I ate {x} apple.")
else:
    print(f"Today, I ate {x} apples.")

#==============洛谷团队系统=================n=int(input())
t=n*5
s=n*3+11
if t<s:
    print("Local")
else:
    print("Luogu")

#==============肥胖问题=====================
m,h=map(float,input().split())
bmi=m/h**2
if bmi<18.5:
    print("Underweight")
elif 18.5<=bmi<24:
    print("Normal")
else:
    print("{0:6g}".format(bmi))
    print("Overweight")
