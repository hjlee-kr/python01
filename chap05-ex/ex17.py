# Q17. 5명에게 할 일 부여하기
# 5명에 한가지씩 일은 분배하고 남는사람은 휴식을 취합니다.
import random
import itertools

people = ['김승현', '김진호', '강춘자', '이예준', '김현주']
job = ['청소', '빨래', '설거지']

# 순서를 섞는다.
people = random.sample(people, len(people))
print(people)
result = itertools.zip_longest(people, job, fillvalue='휴식')
for r in result:
    print(r)
