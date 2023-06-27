from random import *

print(random()) # 0~1 사이의 난수 생성
print(random() * 10) # 0~10 사이의 난수 생성
print(int(random() * 10)) #소수점 자리를 제외한 0~10 사이의 난수 생성
print(int(random() * 10)) #소수점 자리를 제외한 0~10 사이의 난수 생성
print(int(random() * 10)) #소수점 자리를 제외한 0~10 사이의 난수 생성

print(int(random() * 45) + 1) # 1 ~ 45 사이의 난수 생성
#same as
print(randrange(1, 46)) #1 ~ 46 미만의 임의의 난수 생성
#same as
print(randint(1, 45)) # 1이상, 45 이하의 임의의 난수 생성