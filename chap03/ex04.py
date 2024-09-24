# Q4 for문 사용해 1부터 100까지의 숫자를 출력해보자
# 출력형태는 1,2,3,....,100
for i in range(1, 101):
    if i == 100:
        print(i)
    else:
        print(i, end=",")
print("프로그램종료")