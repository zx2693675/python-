# 作者：周祥

age_of_周丹丹 = 27


count = 0
while count <3:
    guess_age = int(input("guess age："))
    if guess_age == age_of_周丹丹:
        print("恭喜你猜对了")
        break
    elif guess_age > age_of_周丹丹:
        print("猜小一点...")
    else:
        print("猜大一点")
    count +=1
else:
    print("你已经试过很多次了。滚蛋")