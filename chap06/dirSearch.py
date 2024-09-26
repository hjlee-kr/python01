# 디렉토리 검색
# 시작디렉토리부터 하위디렉토리 전부검색
# 확장자가 .py만
import os

def search(dirName):
    try:
        fileNames = os.listdir(dirName)
        for fileName in fileNames:
            full_fileName = os.path.join(dirName, fileName)
            if os.path.isdir(full_fileName): # 디렉토리인지?
                search(full_fileName) # 재귀함수(함수자신을 다시호출)
            else:
                ext = os.path.splitext(full_fileName)[-1] #뒤에서 부터 .이 나올때까지
                if ext == '.py':
                    print(full_fileName)
    except PermissionError as e:
        print(e)


search('D:/hjlee/workspaces/python01')