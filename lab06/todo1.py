from nltk import word_tokenize
from nltk.util import ngrams
from nltk.corpus import inaugural

file_content=inaugural.raw('2009-Obama.txt')

tokens = word_tokenize(file_content)
print('\nTokens List:\n')
print(set(list(tokens)))
length=len(list(tokens))
result=list()
gramslist=ngrams(tokens,1)
dictionary={}
for gram in gramslist:
	if str(gram) in dictionary:
		dictionary[str(gram)]+=1
	else:
		dictionary[str(gram)]=1
print(len(dictionary))
