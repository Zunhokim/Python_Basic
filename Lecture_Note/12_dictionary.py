#dictionary는 {}로 표현

cabinet = {3:"유재석", 100:"김태호"}

#dictionary의 값을 가져오는 두 가지 방법
print(cabinet[3]) # 이 경우, n번 위치에 데이터가 존재하지 않을 경우, 에러가 발생하며 프로그램이 종료됨. 
print(cabinet.get(3)) # 이 경우, n번 위치에 데이터가 존재하지 않더라도, None이라고 안내하고, 그 다음 줄을 계속 실행함.

print(cabinet.get(5, "Available")) # 5번 위치에 데이터가 없으므로, 5번 위치는 Available 이라는 메시지 출력

print(3 in cabinet) # 3이라는 변수 안에 데이터가 존재 하는가? >> True
print(5 in cabinet) # 5라는 변수 안에 데이터가 존재하는가?? >> False

# dictionary name[variable] = "data" >> how to add data in dictionary
cabinet[5] = "조세호" # 5라는 변수 내에 조세호라는 데이터 추가
print(cabinet)

# del dictionary name[variable] >> how to delete data in dictionary
del cabinet[100] # 100이라는 변수 내의 데이터 제거
print(cabinet)

print(cabinet.keys()) # print only varible
print(cabinet.values()) # print only data
print(cabinet.items()) # print both

cabinet.clear() # Delete all
print(cabinet)