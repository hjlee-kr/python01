# while문 처리중 while문의 처음으로 돌아가는 명령문
# 1~10 숫자중 홀수만 출력하는 프로그램
num = 0
while num < 10:
    num = num + 1
    if num % 2 == 0: continue # num이 짝수이면 while문의 처음으로 가세요
    print(num)

print("프로그램종료")

# 무한루프에서 강제로 빠져나오는 명령은 키보드로 ctrl+c 를 누르면 됩니다.