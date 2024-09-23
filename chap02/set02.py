# 집합자료형: 합집합, 교집합, 차집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
# 교집합 (s1에도 있고, s2에도 있는 값)
s3 = s1 & s2
print(s3)
# 합집합 (s1에 있거나, s2에 있는 값)
s3 = s1 | s2
print(s3)
# 차집합 (s1의 집합에서 s2에 있는 요소를 제거한 값)
s3 = s1 - s2
print(s3)
s3 = s2 - s1
print(s3)
print("="*50)
# 값추가 - 1개 add()
print(s1)
s1.add(7)
print(s1)
# 값추가 - 여러개 update(A) - A는 리스트나 문자열
s1.update([8,9,10])
print(s1)
# 삭제 - remove
s1.remove(3)
print(s1)
