print("a"+"b")
print("a", "b")

#solution 1
print("나는 %d살입니다." % 20) # %d는 정수형을 의미. 
print("나는 %s을 좋아해요" % "Python") # %s는 문자열을 의미.
print("Apple은 %c로 시작해요" % "A") # %c는 문자형을 의미
    #다중 변수
print("%d살인 나는 %s를 좋아한다. " % (20, "Apple"))

#solution 2
print("나는 {} 살 입니다. ".format(20))
print("나는 {} 살 이고, {} 팀을 좋아한다.".format(24, "Real Madrid"))

#solution 3
print("나는 {num} 살 이고, {team} 팀을 좋아한다.".format(num = 24, team = "Real Madrid"))

#solution 4(ver 3.6 up)
age = 24
teamm = "Real Madrid"
print(f"나는 {age} 살 이고, {teamm} 팀을 좋아한다.")

