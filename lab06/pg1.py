from nltk import word_tokenize

file_content = open("input_text1.txt").read()
wordlist = word_tokenize(file_content)

print('\nTokens List:\n')
print(wordlist)

def getNGrams(input_list, n):
    print('\n',n,'_Grams:\n')
    return [input_list[i:i+n] for i in range(len(input_list)-(n-1))]

print(getNGrams(wordlist, 3))
