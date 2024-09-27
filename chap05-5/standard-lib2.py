# os 모듈
# os 자원 사용 할 수 있도록 하는 모듈
import os
result = os.environ # 환경변수
print(result)

# 디렉토리 위치변경
# os.chdir("c:\windows")

# 시스템 명령어사용
os.system("dir")

"""
os.mkdir() : 디렉토리 생성
os.rmdir() : 디렉토리 삭제
os.remove() : 파일삭제
os.rename() : 파일이름변경
"""

# zipfile 모듈 
import zipfile

#with zipfile.ZipFile('mytest.zip', 'w') as myzip:
#    myzip.write("test.txt")
#    myzip.write("test2.txt")
#   myzip.write("새파일.txt")

# with zipfile.ZipFile('mytest.zip') as myzip:
#     myzip.extractall()
