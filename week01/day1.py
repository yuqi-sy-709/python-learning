# Day 1 作业：凭记忆亲手敲「温度转换」
# 规则：不看视频、不打开 temp_convert.py，自己从头敲到能跑通
#TempConvert.py
TempStr = input("请输入带有温度符号的温度值：")
if TempStr[-1] in ('F','f'):
    C = (eval(TempStr[0:-1])-32)/1.8
    print("转化后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ('C','c'):
    F = eval(TempStr[0:-1])*1.8+32
    print("转化后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")