# 구구단 : 같은단은 한줄에 보여주고,
# 구구단 결과만 출력
# print() 함수에 대한 설명
# print함수에는 기본값으로 end="\n"이 포함되어있다.
# 출력후 다른라인으로 가지 않으려면 end의 값을 변경해주면 됩니다.
for dan in range(2,10):  # 2단부터 9단까지
    print("%d단:" %dan, end=" ")
    for num in range(1,10): # 곱해지는수는 1부터 9까지
        print(dan*num, end=" ")
    print()

print("프로그램 종료")