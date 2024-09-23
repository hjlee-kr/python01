# 리스트 수정 및 삭제
list1 = [1,2,3,4,5]
list1[2] = 6 # list1[2]=3 -> 6 으로 변경
print(list1)
del list1[2]
print(list1)
# 리스트에 관련된 함수
# 리스트에 추가
list1.append(6)
print(list1)
list1.append("lee")
print(list1)
# 리스트 정렬
# 주의사항 자료형이 동일되어야한다.
del list1[5]
list1 = [3,6,1,8,2,4]
print(list1)
list1.sort()
print(list1)
# 뒤집기
list1.reverse()
print(list1)
# 인덱스 반환(return)
num = list1.index(8)
# index안에 적은 값이 list에 없으면 Error발생
# index()를 사용할 때는 예외처리를 해서 사용해야 합니다.
print(num)
# list 중간에 값을 넣고 싶다 - insert()
list1 = [1,2,3,4,5]
print(list1)
list1.insert(1, 6)
print(list1)
# list의 요소 제거 -> remove()
list1.remove(4)
# 없으면 Error발생 -> 예외처리사용
print(list1)
# 맨뒤의 요소를 꺼낸다. -> pop()
num = list1.pop()
print(num)
print(list1)
# count()
list1 = [1,2,3,1,4,5,6,7,1]
print(list1)
num = list1.count(1) # 1이 리스트에 몇개 인지 리턴
print(num)
list1 = ["123", "234", "346", "123"]
print(list1)
num = list1.count("123")
print(num)
# extend() - () 안의 값은 리스트만 올 수 있다.
# 기본리스트에 리스트항목을 추가
list1 = [1,2,3]
print(list1)
list1.extend([4,5])
print(list1)