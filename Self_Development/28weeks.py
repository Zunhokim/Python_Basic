#카카오뱅크 28주 적금 프로그램 작성 (230627)
#7-1장 함수까지 들은 내용을 기반으로 작성됨.

def kakao (week, amount):
    deposit = 0
    plus = 0

    for i in range (week):
        deposit += amount
        plus += deposit

    interest = plus * 0.05

    total = plus + interest

    return total

balance = int(input("Now balance? : "))
amount = int(input("First week deposit amount? : "))
week = 28
total = kakao(week, amount)

print("28 weeks later... Your Balance will be {0} won.".format(balance+total))
print("You got {0} won!".format(total))
