# 5명의 학생점수가 90, 25, 67, 45, 80
# 60점 이상이면 합격, 아니면 불합격 을 출력하는 프로그램 작성
jumsuList = [90, 25, 67, 45, 80]
number = 0 # 학생순서를 알려준다. (학생번호)
for jumsu in jumsuList: #jumsuList 의 인덱싱 순서대로 하나씩 꺼내와서 처리
    number = number + 1
    if jumsu >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

print("프로그램종료")