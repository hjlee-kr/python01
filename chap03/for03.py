jumsuList = [90, 25, 67, 45, 80]
number = 0
for jumsu in jumsuList:
    number = number + 1
    if jumsu < 60: continue # for문 처음으로 돌아가세요
    print("%d번 학생 축하합니다. 합격입니다." % number)

print("프로그램종료")