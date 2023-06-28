#표준 입출력
import sys

print("Python", "Java") # ,는 공백 하나 있는 상태로 이어 출력
print("Python"+"Java") # +는 공백 없이 이어서 출력

print("Python", "Java", sep='\t') # sep=는, seperate의 약자로, 각 구문을 나누는 기준을 만든다. 
print("Python", "Java", sep='\t', end="?") # end=는, 문장의 마지막에 출력할 내용을 담는다. 

print("Python", "Java", file=sys.stdout) # 표준 출력으로 문장 출력
print("Python", "Java", file=sys.stderr) # 표준 에러로 문장 처리

#시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items(): #Dictionary 안의 내용을 불러오기 위해서는 (Dictionary 명).items로 활용해야함
    print(subject.ljust(8), str(score).rjust(8), sep=":") #ljust(n)은, n칸 만큼 공간 확보 후 왼쪽 정렬, rjust(n)은 n칸 만큼 공간 확보 후 오른쪽 정렬

#은행 대기순번표
#001, 002, 003, ...

for num in range(1, 21):
    print("대기번호 : "+str(num).zfill(3)) #.zfill(n)은 n칸 기준, 값이 없는 빈 공간에 대해서는 0으로 채움

answer = input("아무 값이나 입력 : ") #표준 입력, 입력값은 무조건 str 형태로 저장이 됨.