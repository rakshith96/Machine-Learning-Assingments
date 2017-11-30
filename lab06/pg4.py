from nltk import word_tokenize

file_content = open("input_text4.txt").read()
wordlist = word_tokenize(file_content)

print('\nTokens List:\n')
print(wordlist)

def ngrams_prob(lst, n):
    grams = [' '.join(lst[i:i+n]) for i in range(len(lst)-n)]
    print("\n",n,"_Grams:\n")
    print(grams)
    ngramslength=len(grams)
    print("\nNumber of ",n,"_grams = ",len(grams))
    print("\nEach ",n,"_Gram and its Probability:\n")
    t=()
    ngramlist = []
    for gram1 in grams:
        cnt=0
        for gram2 in grams:
            if(gram1==gram2):
               cnt=cnt+1
        t=(gram1,cnt/ngramslength)
        if t not in ngramlist:
            ngramlist.append(t)
    print(ngramlist)       

for i in range(2,4):
   ngrams_prob(wordlist,i)
