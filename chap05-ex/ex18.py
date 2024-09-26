# Q18. 벽에 타일 붙이기
# 가로: 200cm, 세로: 80cm
# 가장 큰 정사각형 모양타일을 붙이려고 합니다.
# 몇 개를 붙여야 할까요?
# 200과 80의 최대공약수
# 가로 갯수 * 세로갯수
import math

width = 200
height = 80

square_size = math.gcd(width, height)
print("타일 한변의 길이 : {}cm".format(square_size))

width_count = width / square_size
height_count = height / square_size

result = int(width_count * height_count)

print("필요한 타일의 갯수 : {}개".format(result))

