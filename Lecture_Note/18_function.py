def open_account():
    print("새로운 계좌가 생성 되었습니다.")

def deposit(balance, money):
    print("입금이 완료 되었습니다.")
    print("현재 잔액 : {0}".format(balance + money))
    return balance + money

balance = 0
balance = deposit(balance, 10000)

print(balance)