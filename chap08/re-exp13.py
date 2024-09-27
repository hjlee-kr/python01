# greedy - * greedy 문자
import re
s = '<html><head><title>Title</title></head></html>'
print(len(s))
print(re.match('<.*>', s).span())
print(re.match('<.*>', s).group())

# non-greedy 쓰고 싶다. ? - non-greedy문자
print(re.match('<.*?>', s).span())
print(re.match('<.*?>', s).group())

