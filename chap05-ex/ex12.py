# Q12. 로또번호 생성하기
import random
# program 1
result = []
while len(result) < 6:
    num = random.randint(1, 45)  # 1부터 45까지 난수발생
    if num not in result:
        result.append(num)

print(result)

# program 2
result = list(range(1,46)) # 1부터 45까지를 리스트로 담는다.
result = random.sample(result, 6)
print(result)
