from nltk.tokenize import sent_tokenize

para = "Hello everyone. It's good to see you. Let's start our text mining class!"
print(sent_tokenize(para))

# Output
# ['Hello everyone.', "It's good to see you.", "Let's start our text mining class!"]