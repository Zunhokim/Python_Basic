#예외 처리
try:
    print("나누기 전용 계산기")
    nums = []
    nums.append(int(input("num1 : ")))
    nums.append(int(input("num2 : ")))
    #nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("Error.")
except ZeroDivisionError as err:
    print(err) # 에러명 출력
except:
    print("?ERROR?")