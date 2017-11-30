from nltk import word_tokenize

file_content = open("input_text2.txt").read()
wordlist = word_tokenize(file_content)

print('\nTokens List:\n')
print(wordlist)

def getNGrams(input_list, n):
  print('\n',n,'_Grams:\n')  
  result=zip(*[input_list[i:] for i in range(n)])
  return result

gram=getNGrams(wordlist, 2)
print(list(gram))
