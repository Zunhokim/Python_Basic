'''
0u1z) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle 과 sample 을 활용

(출력 예제)

--당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
--축하합니다--
'''

# 내가 쓴 답
# import random # shuffle 옵션 사용을 위한 random 함수 import

# user = range(1, 21) # 21 직전 까지인 20까지 숫자 생성
# user = list(user) # 생성된 숫자의 자료구조를 range에서 list로 변경
# random.shuffle(user) # 리스트 순서 섞기

# coffee = [] # 커피 당첨자를 저장할 리스트 생성

# print("--당첨자 발표--")
# print("치킨 당첨자 :", user[0])
# user.pop(0) # 첫 번째 당첨자 제외

# coffee.append(user[0]) # 첫 번째 당첨자를 제외한 항목에서 커피 당첨자 선정
# coffee.append(user[1]) # 첫 번째 당첨자를 제외한 항목에서 커피 당첨자 선정
# coffee.append(user[2]) # 첫 번째 당첨자를 제외한 항목에서 커피 당첨자 선정

# print("커피 당첨자 :", coffee) # 출력 예제에서 커피 당첨자를 리스트 형식으로 출력 했으므로, 커피 당첨자는 리스트 자체를 출력
# print("--축하합니다--")

#정답

import random

user = range(1, 21)
user = list(user)
random.shuffle(user)

winners = random.sample(user, 4) #당첨될 사용자 네명 선정

print("--당첨자 발표--")
print("치킨 당첨자 : {0}".format(winners[0]))
print("치킨 당첨자 : {0}".format(winners[1:]))
print("--축하합니다--")
