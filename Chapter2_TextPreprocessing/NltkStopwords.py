from nltk.corpus import stopwords
# NLTK 제공 불용어 사전

# 영어 불용어만 가져와서 set을 이용해 중복을 제거
english_stops = set(stopwords.words('english’))
text1 = "Sorry, I couldn't go to movie yesterday."
tokens = word_tokenize(text1.lower())
# stopwords를 제외한 단어들만으로 list를 생성
tokens = [word for word in tokens if word not in english_stops]
print(tokens)
# 자신만의 불용어 사전 생성
my_stops = ['could', 'n\'t']
tokens = [word for word in tokens if word not in my_stops]
print(tokens)

# [실행 결과]
# ['sorry', ',', 'could', "n't", 'go', 'movie', 'yesterday', '.']
# ['sorry', ',', 'go', 'movie', 'yesterday', '.']