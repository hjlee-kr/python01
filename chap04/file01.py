# 파일만들기
# f = open("새파일.txt", "w")
# f. close()
# 파일객체 사용법
# 파일객체 = open(파일이름, 파일모드)
# 파일모드: 읽기'r', 쓰기'w', 추가하기'a'
# 한글사용시는 인코딩설정을 해주어야 글자가 깨지지않는다.
f = open("새파일.txt", "w", encoding="utf-8")
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    #data = "%d line." % i
    f.write(data) # data에 있는 값을 파일에 써라
f.close() # 파일사용이 끝나면 반드시 close해줘라.