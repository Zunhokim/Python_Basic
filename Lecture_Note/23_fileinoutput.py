# score_file = open("score.txt", "w", encoding="utf8")
# # score.txt 파일을 열고, 쓰기 목적으로 연다. utf8로 인코딩 (한글 깨짐 방지)

# print("Math : 0", file=score_file)
# print("Eng : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8") # a = append
# score_file.write("Science : 80")
# score_file.write("\nProgramming : 100") # append에서는 줄바꿈을 따로 해줘야함
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf=8")
# print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="") # 줄별로 읽기
# print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# score_file.close()

# 파일의 줄 수가 몇 줄인지 모를때
# score_file = open("score.txt", "r", encoding="utf=8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

score_file = open("score.txt", "r", encoding="utf=8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()
