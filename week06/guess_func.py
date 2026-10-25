import random
def judge(guess,answer):
    if guess<answer:
        return "小了"
    elif guess>answer:
        return "大了"
    else:
        return "对了"

def play():
    answer=random.randint(1,100)
    changes=7
    score=100
    for i in range(changes):
        guess=int(input("请输入你猜的数字："))
        result=judge(guess,answer)
        print(result)
        if result=="对了":
            print(f"猜中！得分{score}")
            return
        score-=10
    print(f"次数用完了，答案是{answer}")
play()
