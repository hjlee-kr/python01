# Q15. 청소당번 2명 뽑기
import itertools

students = ['나지혜', '성성민', '윤지현', '김정숙']
result = itertools.combinations(students, 2)
print(list(result))
