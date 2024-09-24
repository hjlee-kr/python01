# Q2: 1부터 1000까지 3의배수의 합

# while
result = 0  # 결과를 담을 변수
i = 1
while i <= 1000:
    if i % 3 == 0:
        result = result + i
    i += 1  # i = i + 1 같은의미
print("1부터 1000까지 숫자중 3의 배수의 합 : %d" %result)

# for
result = 0
for i in range(1,1001):
    if i % 3 == 0:
        result += i
print("1부터 1000까지 숫자중 3의 배수의 합 : %d" %result)
