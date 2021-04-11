
import dill

filename = 'ngram_model_final.pkl'

with open(filename, 'rb') as fin:
	model = dill.load(fin)

print(len(model.vocab))


def predict(model,context,smoothing=0):
    words_pred=[]
    for word in list(model.counts[1]):
        tem=(word,model.score(word,context.split()))
        words_pred.append(tem)
    words_pred.sort(key = lambda x:x[0],reverse=True)
    return words_pred[:6]


# print(predict(model,'what is your'))
