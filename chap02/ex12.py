a = b = [1,2,3]
a[1] = 4
print(b) # [1,4,3]

# 이유는 a와 b의 주소값(id)가 같기 때문이다.
# a의 요소를 변경하면 b도 같이 변한다
# 반대로 b를 변경하면 a도 변한다.
print("a의 id = " + str(id(a)))
print("b의 id = " + str(id(b)))
