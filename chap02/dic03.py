# 딕셔너리 관련 함수
dic1 = {"name": "lee", "phone":"010-1234-1234", "age":30}
# key 값만 알고 싶어요 - keys()
result = dic1.keys()
print(result)
# key값을 리스트로 담고 싶을때는?
result = list(dic1.keys())
print(result)
# value 값을 알고 싶어요 - values()
result = dic1.values()
print(result)
# value 값을 리스트로 담고 싶을때는?
result = list(dic1.values())
print(result)
# 둘다 알고 싶어요 - items()
result = dic1.items()
print(result)
# key와 value모두를 지우고 싶을때 - clear()
dic1.clear()
print(dic1)
# key로 value를 얻는 함수 - get()
dic1 = {"name": "lee", "phone":"010-1234-1234", "age":30}
result = dic1.get("name") # dic1.get("name") == dic1["name"]
print(result)
# get() 에서 키값이 없으면 None을 리턴, []에서 key값이 없으면 Error
result = dic1.get("birth")
print(result)
# result = dic1["birth"] # Error
# print(result)
# 해당 key가 있는지 조사하는 방법
result = "name" in dic1  # in ~안에 있냐?
print(result) # True
result = "birth" in dic1
print(result) # False
