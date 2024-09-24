# 파일에 데이터 추가하기
f = open("새파일.txt", "a", encoding="utf-8")
for i in range(11, 21):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()