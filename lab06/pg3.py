from nltk import word_tokenize

file_content = open("input_text3.txt").read()
wordlist = word_tokenize(file_content)

print('\nTokens List:\n')
print(wordlist)

def ngrams_count(lst, n):
    counts = dict()
    grams = [' '.join(lst[i:i+n]) for i in range(len(lst)-n)]
    print('\n',n,'_Grams:\n')
    print(grams)
    print("\nN_Grams Count:\n")
    for gram in grams:
        if gram not in counts:
            counts[gram] = 1
        else:
            counts[gram] += 1
    return counts

print(ngrams_count(wordlist, 3))
