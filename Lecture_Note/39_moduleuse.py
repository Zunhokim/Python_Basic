# import theater_module
# theater_module.price(3) # 3인 일반가
# theater_module.price_morning(2) #2인 조조할인가
# theater_module.price_soldier(5) #5인 군인할인가

# 또 다른 모듈 호출 방식
# import theater_module as mv
# mv.price_soldier(3) #mv라는 별명을 통한 모듈의 호출

# 또 다른 방식
# from theater_module import *
# price(3)
# price_soldier(3)
# price_morning(100)

from theater_module import price, price_morning
# 명시된 함수만 가져와 사용하겠다.
price_morning(1200)
price(3)

from theater_module import price_soldier as army
# 하나의 함수만 가져올 떄는 이름을 지정하여 사용 가능함. 
army(100)