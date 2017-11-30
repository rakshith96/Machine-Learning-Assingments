from nltk import word_tokenize
from nltk.util import ngrams

file_content = open("input_text5.txt").read()
tokens = word_tokenize(file_content)
print('\nTokens List:\n')
print(tokens)

for i in range(2,4):
    print('\n',i,'_Grams:\n')
    gramslist=ngrams(tokens,i)
    for gram in gramslist:
        print(gram)
