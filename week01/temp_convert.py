# 温度转换（嵩天 MOOC 第一个案例：摄氏度 C 与华氏度 F 互转）
# 规则：末尾为 F/f 表示华氏度输入，转摄氏度；末尾为 C/c 表示摄氏度输入，转华氏度
val = input("请输入带单位的温度（如 32C 或 89F）：")
if val[-1] in ["F", "f"]:
    c = (float(val[0:-1]) - 32) / 1.8
    print(f"转换后的温度为 {c:.2f}C")
elif val[-1] in ["C", "c"]:
    f = float(val[0:-1]) * 1.8 + 32
    print(f"转换后的温度为 {f:.2f}F")
else:
    print("输入格式错误：温度末尾必须是 C 或 F")
