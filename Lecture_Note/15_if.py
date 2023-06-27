weather = input("Todays weather? : ")

if weather == "비" or weather == "눈":
    print("우산 챙기세요")
elif weather == "맑음":
    print("선크림 바르세요")
elif weather == "미세먼지":
    print("마스크 착용")
else:
    print("잘못된 날씨")