#import 구문에서는 클래스 내의 함수를 바로 사용이 불가능함. 
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

#from () import () 구문에서는 ~~에서 ~~함수를 import 하는 것이므로 바로 사용이 가능함. 
# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip = vietnam.VietnamPackage()
# trip.detail()

from travel import * # travel 폴더 안의 모든 페키지를 가져오곘음

trip = vietnam.VietnamPackage()
trip.detail()
trip2 = thailand.ThailandPackage()
trip2.detail()