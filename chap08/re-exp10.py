# 부정형 전방탐색

"""
.*[.].*$ => 파일이름.확장자
bat 파일은 빼주세요
.*[.](?!bat$).*$
여기에 추가로 exe도 빼주세요
.*[.](?!bat$|exe$).*$
"""