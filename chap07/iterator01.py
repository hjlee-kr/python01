# 이터레이터
"""
리스트, 튜플 - iterable(반복가능)객체
이터레이터는 next()함수 호출시 값을 꺼낼 수 있는 객체
"""
a = [1,2,3] # list는 iterator 가 아니다.
ia = iter(a) # list가 iterator로 바뀐다.
print(next(ia)) # 앞에있는것 하나를 꺼낸다.
print(next(ia))
print(next(ia))
# print(next(ia)) # 네번째 사용할 때 Error발생

print('='*50) # =을 50개 출력
a = [1,2,3]
ia = iter(a)
for i in ia: # for 문을 사용해도 next()를 사용한것과 동일하다.
    print(i)

for i in ia:
    print(i)
