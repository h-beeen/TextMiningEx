import tensorflow as tf
from nltk.tokenize import sent_tokenize

para = "Hello everyone. It's good to see you. Let's start our text mining class!"
print(sent_tokenize(para))