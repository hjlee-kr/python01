# 딕셔너리 자료형 (key, value)
# java의 hashmap과 비슷한 자료형
# web에서 request 나, session에 담을때 사용하는 방법
# {key1:value1, key2:value2, key3:value3, ....}
# key값을 중복을 허용하지 않는다.
dic1 = {'name':'lee', 'age':30, 'phone':'010-1234-1234'}
dic2 = {1:'lee', 2:30, 3:'010-1234-1234'}
print(dic1)
print(dic2)
# 딕셔너리에서 자료 꺼내는 방법 - 대괄호안에 키값을 적어준다.
# 키값에 매칭되는 value를 리턴합니다.
print(dic1['name'])
print(dic2[1])