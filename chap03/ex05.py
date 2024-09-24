# Q5: 평균 점수 구하기
# 값을 전부 더하고 (for, while)
# 더한값을 나눈다
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100, 50, 12]
total = 0       # 더한값을 모아두는 변수
for score in A:
    total += score
average = total / len(A)
print("A학급의 평균점수는 : %s" % average)