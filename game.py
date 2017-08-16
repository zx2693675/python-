# 作者：周祥


age_of_周丹丹 = 27

count = 0
while count <5:
    guess_age = int(input('guess_age:'))
    if guess_age == age_of_周丹丹 :
        print('yes you got it')
        break
    elif guess_age > age_of_周丹丹:
        print('think smaller...')
    else:
        print('think bigger!')
    count +=1
else:
    print('you have tried too many times..fuck off')