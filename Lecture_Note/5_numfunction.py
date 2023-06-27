print(abs(-5)) # 절댓값 출력 함수
print(pow(4, 2)) # a의 b승
print(max(5, 12)) # 최댓값 출력 함수
print(min(5, 12)) # 최솟값 출력 함수
print(round(3.14)) # 반올림

import math
print(math.floor(4.99)) # 내림
print(math.ceil(3.14)) # 올림

from math import *
print(sqrt(16)) # n의 제곱근 출력


# 일반적인 import를 통한 라이브러리 호출은, (라이브러리 명).함수명 의 구조로 사용해야 한다. 
# 그에 반해, from (라이브러리 명) import *의 형식으로 라이브러리를 호출할 경우, 해당 라이브러리 내에 있는 함수를 바로 사용할 수 있다. 