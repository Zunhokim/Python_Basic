subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호는 몇번째 칸?
print(subway.index("조세호"))

# 하하가 탑승
subway.append("하하")
print(subway)

#정형돈이 유재석 뒤에 탑승
subway.insert(1, "정형돈")
print(subway)

#뒤에서부터 한명 내림
print("내린사람 : " +str(subway.pop()))
print(subway)

#같은 이름의 사람은 몇 명?
subway.append("유재석")
print(subway.count("유재석"))

#오름차순 정렬
num_list = [5,2,3,1,4]
num_list.sort()

print(num_list)

#순서 뒤집기
num_list.reverse()
print(num_list)

#다양한 자료형을 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)

#리스트 확장
num_list.extend(mix_list)
print(num_list)
