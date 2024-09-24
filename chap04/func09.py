# 매개변수의 초기값 설정
# 초기값이 있는 함수를 만들때 주의사항
# 초기값이 있는 매개변수 제일 마지막에 만들어준다.
def say_myself(name, age, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d 살 입니다." % age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("홍길동", 20, True)
say_myself("홍길동", 20)
say_myself("신사임당", 50, False)

# def say_myself2(name, man=True, age)