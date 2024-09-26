# Q9. 디렉터리 이동하고 파일목록 출력하기
import os
os.chdir('D:/hjlee/workspaces/python01/chap05-7')
result = os.popen('dir')
# os모듈에서 시스템명령을 사용할때 사용 popen()
# 리턴값은 실행한 결과값
print(result.read())