# 집합자료형
# 집합자료형을 만드는 방법
s1 = set([1,2,3]) # 리스트를 넣는다.
s2 = set("hello") # 문자열을 넣는다.
print(s1)
print(s2)
# 집합자료형의 특징
# 1. 순서가 없다. (인덱싱이 허용되지 않는다.) - 인덱싱되게 하려면 list로 변경해서 쓴다.
# 2. 중복값을 허용하지 않는다.
result = list(s2)
print(result)
print(result[0])