import sympy
x, y = sympy.symbols('x y')
f1 = sympy.Eq(x+y, 10)
f2 = sympy.Eq(x-y, 4)
result = sympy.solve([f1, f2])
print(result)
# 미지수가 여러개일때는 결과값이 딕셔너리 형태로 담긴다.