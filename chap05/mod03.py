# mod01 모듈의 add 함수를 사용할 것입니다.
# 이때는 모듈.add 가 아니고
# add() 처럼 함수이름을 바로 사용할 수 있습니다.
# from mod01 import add
# add, sub를 쓰고 싶다.
# from mod01 import add, sub
# 모든 함수를 다 사용하고 싶다
from mod01 import *


print(add(4,5))
print(sub(4,5))