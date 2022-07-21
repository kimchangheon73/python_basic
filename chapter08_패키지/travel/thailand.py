class Thailand:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콩, 파타야 영행 (야시장 투어)50만원")
        


# 파일 내부/외부 호출 여부 
if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행됩니다")
    trip_to = Thailand()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")