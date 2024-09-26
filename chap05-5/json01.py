# json 파일을 딕셔너리형태로 변환
import json

with open('chap05-5/myinfo.json', encoding="utf-8") as f:
    data = json.load(f)

print(type(data))
print(data)

data["성별"] = "남자" # dict 데이터에 추가
with open('chap05-5/myinfo.json', 'w', encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# ensure_ascii=False => 한글형태 그대로 만듬 (기본은 unicode값)
# indent=4 => 들여쓰기지정
