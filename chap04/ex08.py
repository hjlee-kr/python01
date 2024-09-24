# Q8. 입력값을 모두 더해서 출력하기 sys
import sys

args = sys.argv[1:]
result = 0
for i in args:
    result += int(i)

print(result)