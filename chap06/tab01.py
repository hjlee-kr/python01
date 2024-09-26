# tab으로 되어있는 부분을 공백문자(space) 4개로 변경하는 프로그램
# 파일을 읽고, 다른파일에 저장

import sys

src = sys.argv[1]
dst = sys.argv[2]

with open(src, 'r', encoding='utf-8') as f:
    tab_content = f.read()

space_content = tab_content.replace('\t', ' '*4)

with open(dst, 'w', encoding='utf-8') as f:
    f.write(space_content)

print("프로그램종료")

# print(src)
# print(dst)
# 1. sys module 사용
# file 관련 처리문을 사용
# replace(A, B) 함수 사용 - A를 찾아서 B로 변경