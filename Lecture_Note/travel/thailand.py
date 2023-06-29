class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")

if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행 됩니다. ")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")

#모듈의 직접 실행 예시.
#모듈 파일 내에서 디버그 및 실행을 할 경우 안에 있는 내용이 나옴.
#모듈 직접 실행 시 결과는 __name__ == "__main__" 내에 적으면 됨. 