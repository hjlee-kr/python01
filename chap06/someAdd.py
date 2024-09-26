# 1000미만의 자연수에서 3과 5의 배수를 모두 더하는
# 프로그램을 작성하세요
result = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        result += i

print("1000미만 자연수 중 3또는 5의 배수의 합은 : %d" % result)

# 프로젝트 오일러 site의 첫번째 문제였습니다.