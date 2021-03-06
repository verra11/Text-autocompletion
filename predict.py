
import dill
import nltk
import time

pre=time.time()

print('starting')

filename = 'ngram_model.pkl'

with open(filename, 'rb') as fin:
	model = dill.load(fin)

#predicts next word
def predict(context,smoothing=0):
    words_pred_uni=[]
    words_pred_bi=[]
    words_pred_tri=[]
    tgram=context
    bgram=' '.join(context.split()[1:])
    ugram=' '.join(context.split()[2:])
    
#     print(tgram,'\n',bgram,'\n',ugram)
    for word in list(model.counts[1]):
        if(word=='<s>' or word=='</s>' or word=='<UNK>'):
            continue
        tem=(model.score(word,tgram.split()), word)
        words_pred_tri.append(tem)
        tem=(model.score(word,bgram.split()), word)
        words_pred_bi.append(tem)
        tem=(model.score(word,ugram.split()), word)
        words_pred_uni.append(tem)
        
    words_pred_tri.sort(key = lambda x:x[0],reverse=True)
    words_pred_bi.sort(key = lambda x:x[0],reverse=True)
    words_pred_uni.sort(key = lambda x:x[0],reverse=True)
    words_pred=[]
    for i in range(9):
        words_pred.append(words_pred_tri[i])
    
    if(smoothing==0):
        return words_pred
    
    if(words_pred[-1][0]!=0.0):
        print('from trigrams')
        return words_pred
    
    words_pred=[]
    for i in range(9):
        words_pred.append(words_pred_bi[i])
    if(words_pred[-1][0]!=0.0):
        print('from bigrams')
        return words_pred
    
    print('from unigrams')
    return words_pred_uni[:9]

#auto completess the current word
def predict_now(context,current_word):
    bgram=context.split()[-2:][0]
    words_pred_bi=[]
    words_pred_edi=[]
    for word in list(model.counts[1]):
        if(word=='<UNK' or word=='<s>' or word=='</s>' or word.startswith(current_word)!=True):
            continue
        tem=(model.score(word,bgram.split()), word)
        words_pred_bi.append(tem)
        tem=(nltk.edit_distance(word,current_word, transpositions=True),word)
        words_pred_edi.append(tem)
        
    words_pred_bi.sort(key = lambda x:x[0],reverse=True)
    words_pred_edi.sort(key = lambda x:x[0])    
    words_pred=words_pred_bi[:3]+words_pred_edi[:2]
    return words_pred

#corrects the current word
def crct_word(current_word):
    words_pred=[]
    for word in list(model.counts[1]):
        if(word=='<UNK' or word=='<s>' or word=='</s>' ):
            continue
        tem=(nltk.edit_distance(word,current_word, transpositions=True),word)
        words_pred.append(tem)
    words_pred.sort(key = lambda x:x[0])
    return words_pred[:3]

# print(list(brown.words())[:20])
# print(model.counts[['an','investigation','of']]['atlanta\'s'])
# print(predict('the adventures of'))
# print(predict_now('what are','cont'))
# print(crct_word('hllo'))

print('ended',time.time()-pre)

