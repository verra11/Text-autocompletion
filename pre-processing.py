from nltk.tokenize import word_tokenize, sent_tokenize

file = open(r'corpus.txt', 'r')
text = file.read()
file.close()

tokenized_text = [list(map(str.lower, word_tokenize(sent)))
					for sent in sent_tokenize(text)]


print(tokenized_text[0])