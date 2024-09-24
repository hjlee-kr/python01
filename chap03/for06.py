# 리스트 컴프리헨션 사용하기

# 리스트안에 숫자에 각각 3을 곱하고 리스트로 저장후 출력
# 일반적인 for
numList = [1,2,3,4]
result = []
for num in numList:
    result.append(num*3)
print(result)

# 리스트 컴프리헨션
numList = [1,2,3,4]
result = [num*3 for num in numList]
print(result)

# 짝수만 3을 곱하고 싶을때
numList = [1,2,3,4]
result = [num*3 for num in numList if num % 2 == 0]
print(result)

# 구구단을 리스트에 넣고 싶다.
result = [dan*num for dan in range(2,10)
                  for num in range(1,10)]
print(result)
