# 지역변수 : 함수 내에서만 사용 되는 변수
# 전역변수 : 프로그램 전체에서 부를 수 있는 전역 변수

gun = 10

def checkpoint(soldiers): # 경계근무 인원
    global gun # 전역 변수 gun 호출
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))

# 가급적 전달값으로 계산하는 방향이 좋음