"""
시윤이가 가진돈의 2/5로 학용품을 샀습니다.
이때 쓴돈이 1760원입니다.
그러면 남은돈은 얼마일까요?
"""
from fractions import Fraction
import sympy

# 가지고 있던 돈을 x라고 하자.
x = sympy.symbols("x")

# Fraction()은 정확한 유리수계산을 위해 사용
# x * (2/5) = 1760
f = sympy.Eq(x*Fraction('2/5'), 1760)

# 방정식의 결과를 구하는 것 - 리턴값은 리스트
result = sympy.solve(f)

# 남은 돈은 전체금액에서 사용한 금액을 뺀다.
remains = result[0] - 1760

print("남은돈은 {}원입니다.".format(remains))
