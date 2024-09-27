import re

p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())
# http:

# : 을 제외하고 매치되는 것을 리턴하고 싶을때
# http: -> http 리턴
p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())
# http
# 검색에는 포함되지만 결과에는 제외된
# ?=: 을 사용한 방식을 긍정형 전방 탐색
