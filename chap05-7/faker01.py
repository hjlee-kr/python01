from faker import Faker
fake = Faker('ko-KR') # 한글데이터가 나오도록 설정
result = fake.name() # 이름을 리턴
print(result)
result = fake.address() # 주소를 리턴
print(result)

# 30건의 데이터 저장 : 이름, 주소를 가진
test_data = [(fake.name(), fake.address()) for i in range(30)]
print(test_data)

# 점프투 파이썬 P290 에 사용할 수 있는 대표적인것 기록