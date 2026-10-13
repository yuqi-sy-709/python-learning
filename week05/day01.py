# 中国bmi标准 复杂度O(1)
h,w=eval(input("请输入您的身高（米）和体重（千克）（逗号隔开）："))
bmi=w/h**2
print("您的 BMI 值为：",bmi)
who=""
if bmi<18.5:
    who="偏瘦"
elif 18.8<=bmi<=23.9:
    who="正常"
elif 24.0<=bmi<=27.9:
    who="过重"
elif 28.0<=bmi<=31.9:
    who="肥胖"
elif bmi>=32.0:
    who="严重肥胖"
print(who)

# 计算圆周率 复杂度O(n)
pi=0
N=100
for i in range(0,N):
    pi+=1/pow(16,i)*(4/(8*i+1)-2/(8*i+4)-1/(8*i+5)-1/(8*i+6))
print("圆周率值：{}".format(pi))

# 蒙特卡洛算法计算圆周率 复杂度O(n)
#公式：Π=4*（hits/Darts)
from random import random
from time import perf_counter
Darts=1000*1000
hits=0.0
start=perf_counter()
for i in range(1,Darts+1):
    x,y=random(),random()
    d=pow(x**2+y**2,0.5)
    if d<1.0:
        hits+=1
end=perf_counter()
pi=4*(hits/Darts)
print("圆周率值：{}".format(pi))
print("耗时：{}".format(end-start))


