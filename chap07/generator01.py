'''
def mygen():
    for i in range(1, 1000):
        result = i * i
        yield result
gen = mygen()
'''
# 위의 함수와 동일한 튜플표현식 - 리스트 컴프리헨션과 비슷
# "제너레이터 표현식" 이라고 부릅니다. 
gen = (i * i for i in range(1, 1000))

print(next(gen))
print(next(gen))
print(next(gen))
