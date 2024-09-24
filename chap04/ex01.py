# Q1. 홀수, 짝수 판별하기
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False
    
number = int(input("숫자를 입력하세요:"))
result = is_odd(number)
if result:
    print("홀수입니다.")
else:
    print("짝수입니다.")