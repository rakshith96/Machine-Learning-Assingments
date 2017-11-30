from nltk import word_tokenize
from nltk.util import ngrams
from nltk.corpus import inaugural
import operator

file_content1=inaugural.raw('2009-Obama.txt')
file_content2=inaugural.raw('1789-Washington.txt')
tokens1 = word_tokenize(file_content1)
tokens2 = word_tokenize(file_content2)
length1=len(list(tokens1))
length2=len(list(tokens2))
gramslist1=ngrams(tokens1,1)
gramslist2=ngrams(tokens2,1)
dictionary1={}
dictionary2={}
def sort_dict(dictionary):
	res=sorted(dictionary.items(),key=operator.itemgetter(1),reverse=True)
	return res
for gram in gramslist1:
	if str(gram) in dictionary1:
		dictionary1[str(gram)]+=1
	else:
		dictionary1[str(gram)]=1
for gram in gramslist2:
	if str(gram) in dictionary2:
		dictionary2[str(gram)]+=1
	else:
		dictionary2[str(gram)]=1

dictionary1=sort_dict(dictionary1)
dictionary2=sort_dict(dictionary2)

print('obama')
i=0
for key,value in dictionary1:
	if i <50:
		print(key,':',value)
		i+=1
print('washington')
i=0
for key,value in dictionary2:
	if i <50:
		print(key,':',value)
		i+=1
