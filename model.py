from nltk.lm.preprocessing import padded_everygram_pipeline
from preprocessing import processed_text
from nltk.lm import MLE
import dill

n = 3

training_data, padded_sents = padded_everygram_pipeline(n, processed_text)

model = MLE(n)
model.fit(training_data, padded_sents)

filename = 'ngram_model.pkl' 
with open(filename, 'wb') as out:
	dill.dump(model, out)

