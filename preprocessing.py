from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import brown
import string

file = open(r'corpus.txt', 'r')
text = file.read()
file.close()

punctuations = string.punctuation

tokenized_text = [list(map(str.lower, word_tokenize(sent)))
					for sent in sent_tokenize(text)]

brown_corpus = [[word.lower() for word in sent]
				for sent in brown.sents()]

processed_text = []

for sent in tokenized_text:

	plain_text = []
	for word in sent:
		if word in punctuations:
			continue
		plain_text.append(word)
	processed_text.append(plain_text)

for sent in brown_corpus:

	plain_text = []
	for word in sent:
		if word in punctuations:
			continue
		plain_text.append(word)
	processed_text.append(plain_text)

# print(tokenized_text[0])
# print(processed_text[0])

# processed_text is the training data