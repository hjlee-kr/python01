# range(A,B,C), range(A,B), range(B)
# A: 처음숫자, B: 마지막숫자(포함안됨), C: Step 몇개씩 증가할것인지?
# C를 적지않으면 1이 default로 적용
# A를 적지않으면 0이 default
a = range(10)
print(a)

# 1부터 10까지 더한값을 출력
add = 0
for i in range(1, 11):
    add = add + i

print("1부터 10까지 더한값은: %d" %add)

# 2부터 10까지 짝수만 더하기
add = 0
for i in range(2, 11, 2):
    add = add + i
print("2부터 10까지 짝수만 더한값은: %d" % add)

jumsuList = [90, 25, 67, 45, 80]
# len(jumsuList) = 5 이므로 range(5) 와 동일
# number에는 0, 1, 2, 3, 4 가 순서대로 들어가서 처리됩니다.
for number in range(len(jumsuList)):
    if jumsuList[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." %(number+1))
print("프로그램종료")

# 1부터 100까지 더한값을 출력하세요
add = 0
for i in range(1, 101):
    add = add + i
print("1부터 100까지 더한값: %d" %add)