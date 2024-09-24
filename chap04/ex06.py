# Q6. 사용자 입력 지정하기
user_input = input("저장할 내용을 입력하세요:")
f = open('test.txt', "a", encoding="utf-8")
f.write(user_input)
f.write('\n')
f.close()
