import dill

filename = 'ngram_model.pkl'

with open(filename, 'rb') as fin:
	model = dill.load(fin)

print(len(model.vocab))