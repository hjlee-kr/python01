# 튜블 자료형 (리스트와 비슷하나 값을 변경할 수 없다.)
t1 = (1, 2)
t2 = ("lee", "kim")
t3 = 1,2   # 가로없이 사용할 수 있다.
t4 = (1, 2, "lee", "kim")
t5 = (1, 2, (1, 2))
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
# 튜플자료형은 값을 변경할 수 없기 때문에
# 값을 변경하거나 삭제하려고 하면 Error가 발생한다.
# del t1[0]
print("="*50)
# 튜플에서 허용하는 것은 인덱싱, 슬라이싱, 더하기, 곱하기
print(t1[1]) # 2를 출력
print(t5[1:])
print(t1+t4)
print(t1*3)