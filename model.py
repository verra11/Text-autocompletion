
from nltk.lm.preprocessing import padded_everygram_pipeline
from preprocessing import processed_text
from nltk.lm import MLE
from nltk.lm import Vocabulary
import dill
import time

n = 4

training_data, padded_sents = padded_everygram_pipeline(n, processed_text)


pre_tim=time.time()

print('starting training')
print('#######################################')

vocab=Vocabulary(unk_cutoff=2)
model = MLE(n,vocabulary=vocab) 
model.fit(training_data, padded_sents)


print('#######################################')
print('done training', time.time()-pre_tim)


filename = 'ngram_model.pkl' 
with open(filename, 'wb') as out:
	dill.dump(model, out)

print(model.vocab)