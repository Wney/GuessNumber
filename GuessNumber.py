import random
min=0
while True:
    mode = int(input("请输入模式：\n1.默认模式，范围0-100\n2.自定义模式，0-9999\n"))
    if mode==1:
        max=100
        break
    elif mode==2:
        max = int(input("请输入最大值：\n"))
        break

bingo = random.randint(min,max);
while True:
    guess = int(input("请输入一个数：\n"))
    if guess>=max:
        print("请输入比%d小的数\n"%(max))
    elif guess<=min:
        print("请输入比%d大的数\n"%(min))
    else:
        if guess==bingo:
            print("恭喜你，答对了\n")
            break
        elif guess>bingo:
            print("%d到%d\n"%(min,guess))
            max=guess
        elif guess<bingo:
            print("%d到%d\n"%(guess,max))
            min=guess