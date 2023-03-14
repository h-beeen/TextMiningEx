import re
# 둘째 인수인 문자열에서 a, b, c 중 하나라도 일치하는 문자를 가져옴
print(re.findall("[abc]", "How are you, boy?"))
# 숫자를 검색
print(re.findall("[0123456789]", "3a7b5c9d"))

# Output
# ['a', 'b']
# ['3', '7', '5', '9']