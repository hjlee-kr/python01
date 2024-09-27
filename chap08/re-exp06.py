import re

charref = re.compile(r'&[#](0[0-7+|[0-9]+]|x[0-9a-fA-F]+);')

# 정규표현식을 한줄로 표현하려니 해석이 너무 힘들고
# 사용하기도 불편해요
# re.VERBOSE

charref = re.compile(r"""
    &[#]
    (
        0[0-7]+         # 8진수
        | [0-9]+        # 10진수
        | x[0-9a-fA-F]+ # 16진수
    )
    ;
    """, re.VERBOSE)
# re.VERBOSE : 스페이스나 \n등 공백부분을 제거하는 옵션