"""
구구단
키보드로 입력을 받아서 2~9 중 하나를 받아서 출력
출력형태=>2단 : 2 4 6 8 10 12 14 16 18
[메뉴] 몇단을 보여줄까요?(종료는 0):
"""
def gugudan(number):
    result = []
    for i in range(1, 10): # 1부터 9까지 각각 곱한다.
        result.append(number*i) # 단수와 곱해서 리스트에 저장

    str1 = ("%d단 : " % number) + (" ".join(map(str, result)))
    # join() 문자열로된 리스트, 튜플등을 입력값으로 사용합니다.
    # map()는 리스트형의 처리 - str()을 사용하여 int -> str으로 변환
    return str1

print("===구구단 프로그램입니다.===")
while True:
    number = int(input("[메뉴] 출력하고싶은 단수는?(2~9, 0은 종료) : "))
    if number >= 2 and number <= 9:
        # 구구단 출력
        print(gugudan(number))
    elif number == 0:
        # 프로그램 종료
        break;
    else:
        print("잘못입력하셨습니다. 다시입력하세요")

print("프로그램을 종료합니다.")