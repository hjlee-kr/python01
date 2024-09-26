# 문자열 나열하기
import itertools

str1 = "abcd"
result = itertools.permutations(str1, 4)
for r in result:
    print(''.join(r))
