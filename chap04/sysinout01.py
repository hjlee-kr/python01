# sys모듈 사용하기
import sys
args = sys.argv[1:] # 파일썬파일이 0번, 인자들은 1번부터시작
for i in args:
    print(i)
