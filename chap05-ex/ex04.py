# Q4. 음수제거하기
# filter 와 lambda 사용
# filter(함수명, 데이터)
result = list(filter(lambda x : x > 0, [1,-2,3,-5,8,-3]))
print(result)
