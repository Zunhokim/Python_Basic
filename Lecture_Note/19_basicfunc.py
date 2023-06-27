# def profile(name, age, main):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}".format(name, age, main))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")



#같은 학교, 학년, 반, 수업

# def profile(name, age=17, main="파이썬"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}".format(name, age, main))

# profile("유재석")
# profile("김태호")


#가변인자

# def profile(name, age, lang1, lang2, lang3, lang4, lang5): 
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language): 
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JS")
profile("김태호", 23, "Kotlin", "Swift")