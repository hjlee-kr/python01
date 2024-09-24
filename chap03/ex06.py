# 리스트 컴프리헨션 사용하기
# 홀수만 2를 곱한값을 리스트에 담아서 출력
numbers = [1,2,3,4,5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)

print(result)

# 컴프리헨션 사용
numbers = [1,2,3,4,5]
result = [num * 2 for num in numbers if num % 2 == 1]
print(result)