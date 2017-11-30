from nltk import word_tokenize
from nltk.util import ngrams
from nltk.corpus import inaugural
import operator

file_content=inaugural.raw('2009-Obama.txt')
tokens = word_tokenize(file_content)
print('\nTokens List:\n')
print(tokens)
length=len(list(tokens))
result=list()
for i in range(1,4):
    print(str(i)+" gram\n")
    gramslist=ngrams(tokens,i)
    dictionary={}
    for gram in gramslist:
    	if str(gram) in dictionary:
    		dictionary[str(gram)]+=1/float(length-(i-1))
    	else:
    		dictionary[str(gram)]=1/float(length-(i-1))
    print(max(dictionary.items(), key=operator.itemgetter(1))[0])
