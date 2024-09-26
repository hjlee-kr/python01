# 파일을 임시로 만들어서 사용할때 쓰는 모듈
import tempfile
filename = tempfile.mkstemp()
print(filename)