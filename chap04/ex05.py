# Q5. 프로그램 오류 수정하기 2
# 파일을 열었으면 닫아주세요
f1 = open("test.txt", "w")
f1.write("Life is too short.")
f1.close()
f2 = open("test.txt", "r")
print(f2.read())
f2.close()