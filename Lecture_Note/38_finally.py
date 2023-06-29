class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
        
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기")
    num1 = int(input("num1 : "))
    num2 = int(input("num2 : "))
    if num1 >= 10 | num2 >= 10:
        raise BigNumberError("Input : {0} / {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError as err:
    print(err)

except BigNumberError as err:
    print(err)

finally:
    print("Thank you for using.")

#정상 수행 여부에 상관 없이 무조건 동작하는 구문 > finally: