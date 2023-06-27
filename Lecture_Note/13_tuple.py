#튜플은 내용 변경이나 추가를 할수 없음. 
#튜플은 ()로 표현.

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

name = "김종국"
age = 20
hobby = "헬스"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)
