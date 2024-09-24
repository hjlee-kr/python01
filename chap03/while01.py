"""
while문
while 조건:
    처리문
    처리문
    처리문
처리문 => while문이 끝나고 처리하는 곳
"""
treeHit = 0  #나무를 찍은 횟수
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무가 넘어갑니다.")
print("프로그램종료")
