import pickle

# profile_file = open("profile.pickle", "wb") #write binary, pickle을 쓰기 위해선 binary를 정의해야함

# profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

profile_file = open("profile.pickle", "rb") #write binary, pickle을 쓰기 위해선 binary를 정의해야함

profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
profile = pickle.load(profile_file) # 파일의 정보를 profile에 불러오기
print(profile)
profile_file.close()