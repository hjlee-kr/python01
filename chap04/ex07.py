# Q7. 파일의 문자열 바꾸기
# test.txt 파일의 java 문자열을 python으로 변경
f = open("test.txt", "r")
body = f.read()
f.close()
body = body.replace("java", "python")
f = open("test.txt", "w")
f.write(body)
f.close()