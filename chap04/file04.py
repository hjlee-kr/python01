# with예약어 close()를 사용하지 않아도
# with블럭을 벗어나면 자동으로 close()된다.
with open("새파일.txt", "r", encoding="utf-8") as f:
    data = f.read()
    print(data) # 여기까지 진행한후 f.close() 가 자동으로 실행
print("프로그램종료")