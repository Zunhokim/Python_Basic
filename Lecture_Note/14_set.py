# 집합 (set)
# 중복 불가, 순서 없음

my_set = {1,2,3,3,3}
print(my_set)

num = set([1,1,1,1,2,3,4,3,4,4,5,6])
print(num)

java = {"유재석", "김태호", "박명수"}
python = set(["유재석", "김종국", "박명수"])

#java와 python의 교집합 출력
print(java & python)
print(java.intersection(python))

#java와 python의 합집합 출력
print(java | python)
print(java.union(python))

#java와 python의 차집합 출력 (java - python)
print(java - python)
print(java.difference(python))

#python 숙련자 추가
python.add("김태호")
print(python)

#java를 잊어버림
java.remove("김태호")
print(java)