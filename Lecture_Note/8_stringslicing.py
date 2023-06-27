id = "000609-1234567"

print("성별 : "+id[7])
print("년도 : "+id[:2]) #출력할 자리의 마지막 자리 +1
print("생일 : "+id[2:6])
print("뒷자리 : "+id[7:])

# [:n]의 경우, 처음부터 n번째 자리까지 가져옴
# [n:]의 경우, n번째 자리부터, 끝까지 가져옴

#문자열 처리 함수

python = "Python is Amazing"
print(python.lower()) # 문자열 전체를 소문자로
print(python.upper()) # 문자열 전체를 대문자로
print(python[0].isupper()) # n번째 문자가 대문자인가?
print(len(python)) # 문자열의 길이 출력
print(python.replace("Python", "Java")) # A문자열을 B문자열로 대체

index = python.index("n") # n이 문자열 내에서 몇번째에 있는가
print(index)
index = python.index("n", index + 1) # 문자열 내에서 n이 나오는 두번째 위치
print(index)

print(python.find("java")) # java라는 글자가 없으므로, -1이 출력됨. 

#index 함수는 찾는 문자열이 없을 경우, 디버그 에러, 프로그램 중단
#find 함수는 찾는 문자열이 없을 경우, -1 출력. 

print(python.count("n")) # n이 총 몇번 나오는지 계산