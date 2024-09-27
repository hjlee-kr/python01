# 정규표현식
# 메타문자 : . ^ $ * + ? {} [] \ | ()
import re

"""
[] : 한개의 문자
[a-zA-Z0-9], [abc]
[a-zA-Z] : 모든 영문자
[0-9] : 모든 숫자
"""
"""
. : \n을 제외하 모든 문자
a.b : a0b, a3b, atb, ... (o) : abc (x)
".py" -> [.]py : [.]은 모든문자가 아니고 .을 의미합니다.
"""
"""
* : 0개 이상의 문자
ca*t -> ct, cat, caat, caaat, ... (o)
+ : 1개 이상의 문자
ca+t -> cat, caat, caaat, ...(o) : ct (x)
"""
"""
{} : 숫자제한
ca{2}t -> caat (o)
ca{2,5}t -> caat, caaat, caaaat, caaaaat (o) (a를 2~5개)
"""
"""
? : ?앞에 문자가 하나 있거나, 없을때
ca?t -> ct, cat (o)
"""
"""
| : or 의 의미 A|B -> A정규식 또는 B정규식
"""
"""
^ : 문자열의 맨처음을 의미한다.
re.MULTILINE 과 함께 사용하면 라인의 맨처음을 의미
"""
"""
$ : 문자열의 맨 마지막을 의미한다.
re.MULTILINE 과 함께 사용하면 라인의 맨마지막을 의미
"""
"""
\A : 문자열 처음 - re.MULTILINE 과 관계없이
"""
"""
\Z : 문자열 끝 - re.MULTILINE 과 관계없이
"""
"""
\b : 단어 구문자가 있는 매치
"""
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))
"""
\B : 단어구분자가 없는 매치
"""
p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))