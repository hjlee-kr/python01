coffee = 10
money = 300
while money: # money에는 0이 아닌 숫자가 있어서 True입니다. 무한루프로 작동합니다.
    print("돈이 들어왔습니다. 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피는 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break # while문을 벗어납니다.

print("프로그램이 종료됩니다.")