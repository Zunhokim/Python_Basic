'''
Qu1z) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.

50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.
조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[0] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[0] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 16분)
총 탑승 승객 : 2 분
'''

import random

customer = [[0]*2 for i in range (50)]

for i in range (50):
    customer[i][0] = i+1
    customer[i][1] = random.randrange(5, 51)

count = 0
check = 1

while check < 50:
    if 5 <= customer[check][1] <= 15:
        print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format("O", customer[check][0], customer[check][1]))
        count += 1
        check += 1
    else:
        print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(" ", customer[check][0], customer[check][1]))
        check += 1

print("총 탑승 승객 : {0} 분".format(count))