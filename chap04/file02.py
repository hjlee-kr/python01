# 파일을 읽자
f = open("새파일.txt", "r", encoding='utf-8')
line = f.readline() # readline() 한줄 출력
print(line)
f.close

print("="*50)
f = open("새파일.txt", "r", encoding='utf-8')
while True:
    line = f.readline()
    if not line: break
    print(line, end="")
f.close()

print("="*50)
f = open("새파일.txt", "r", encoding='utf-8')
lines = f.readlines()
f.close()
for line in lines:
    print(line, end="")

print("="*50)
f = open("새파일.txt", "r", encoding='utf-8')
for line in f: # 파일객체를 사용하면 한줄단위로 읽어옵니다.
    print(line, end="")
f.close()

print("="*50)
f = open("새파일.txt", "r", encoding='utf-8')
data = f.read() # read()함수 파일에 있는 전체 데이터를 리턴합니다.
f.close()
print(data)
