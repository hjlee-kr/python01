from copy import copy
# 리스트 복사
list1 = [1,2,3]
list2 = list1
print(id(list1))
print(id(list2))
list1[1] = 4
print(list1)
print(list2)
print("="*50)
# 주소값을 다르게 복사하려면
# 1. 슬라이싱이용
list1 = [1,2,3]
list2 = list1[:] # 리스트 전체를 슬라이싱한다.
print(id(list1))
print(id(list2))
list1[1] = 4
print(list1)
print(list2)
print("="*50)
# 2. copy모듈을 사용 => import 해야한다
list1 = [1,2,3]
list2 = copy(list1)
print(id(list1))
print(id(list2))
list1[1] = 4
print(list1)
print(list2)