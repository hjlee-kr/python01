import re

p = re.compile('[a-z]+')
m = p.search('3python') # 정규표현식과 맞는 문자열을 찾는다.
print(m)

result = p.findall("Life is too short")
# 정규표현식과 맞는 문자열을 리스트 type으로 리턴
print(result)

result = p.finditer("Life is too short")
print(result)
for r in result:
    print(r)

# match객체
"""
group() : 매치된 문자열을 리턴
start() : 매치된 문자열의 시작 위치
end() : 매치된 문자열의 끝 위치 - 문자열끝 + 1
span() : 매치된 문자열의 (시작, 끝)을 튜플형태로 리턴
"""