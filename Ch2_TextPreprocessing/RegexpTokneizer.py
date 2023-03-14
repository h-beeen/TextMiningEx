from nltk.tokenize import RegexpTokenizer
text1 = "Sorry, I can't go there."
# 문자, 숫자, 언더바(_), 아포스트로피(＇)로 이루어진 3자 이상의 단어로 토크나이즈
tokenizer = RegexpTokenizer("[\w']{3,}")
print(tokenizer.tokenize(text1.lower())) # 소문자로 바꾸고 정규식 적용

# Output
# ['sorry', "can't", 'there']