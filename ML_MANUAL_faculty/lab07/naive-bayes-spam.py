#spam classification

trainingSetPercentage = 70; # percentage of all data samples used for training
unknownTokenLabel = '<UNK>' # label for unknown tokens in new documents
maxIterations = 5 # iterations to mesure accuracy

def main():
    dataDir = "/home/prd/ML_LAB/ML/spam_reviews"
    iterations = 0
    aveAccuracy = 0
    while iterations < maxIterations:	
        iterations += 1
        print('iteration', iterations, ':')
        trainData, testData = getTrainTestData(dataDir)	
        #print(trainData)
        #print(testData)
        #print('$%$%#',list(trainData.items()))
        priors, wordsLikelihood = train(trainData, dataDir)
        #print(":::::",priors)
        accuracy = test(testData, dataDir, priors, wordsLikelihood)
        aveAccuracy += accuracy
        print('accuracy:', accuracy, '%')		
        #print()
    print('\n')    
    print('final accuracy \n')    
    print('ave_accuracy:', float(aveAccuracy) / iterations, '%')
def train(trainData, dataDir):
    """Train Naive Bayes model"""
    numberOfDocs = getNumberOfDocuments(trainData)
    priors = computePriors(trainData, numberOfDocs)
    #p=print(priors)
	#print('total_num_docs:', numberOfDocs)
    vocabulary = getVocabulary(trainData, dataDir)
    wordsFrequency = getWordsFrequencyPerClass(trainData, dataDir)
    print("^^^",wordsFrequency)
    numberOfWords = getNumberOfWordsPerClass(wordsFrequency)
    wordsLikelihood = computeWordsLikelihood(wordsFrequency, numberOfWords, len(vocabulary))
    #w=print(wordsLikelihood)
    return priors, wordsLikelihood

def test(testData, dataDir, priors, wordsLikelihood):
	"""Returns the accuracy of the model"""
	
	totalCorrectCount = 0
	totalCount = 0

	for realClass, fileList in list(testData.items()):
		classCorrectCount = 0
		for fileName in fileList:
			text = open(dataDir + '/' + realClass + '/' + fileName).read()
			guessedClass = classify(text, priors, wordsLikelihood)
			totalCount += 1
			if guessedClass == realClass:
				classCorrectCount += 1
		
		totalCorrectCount += classCorrectCount
		
		print('num_' + realClass + '_correct_docs:', classCorrectCount)	

	return (float(totalCorrectCount) / totalCount) * float(100)
	

def classify(text, priors, wordsLikelihood):
	"""Classify an instance according to the learned model"""
	import math, sys
	
	# initialize maxLikelihood in the minimum possible value
	maxLikelihood = -sys.maxsize-1
	classification = ''
	for c, prior in list(priors.items()):
		words = tokenize(text)
		
		# preventing underflow with logarithm
		currentLikelihood = float(math.tanh((prior))) 
		#currentLikelihood = float(prior)
			
		for w in words:			
			if w in wordsLikelihood[c]: 
				currentLikelihood += math.log(wordsLikelihood[c][w])
				#currentLikelihood *= wordsLikelihood[c][w]
				
			else: # if w is a new word, use the unknown token likelihood
				currentLikelihood += math.log(wordsLikelihood[c][unknownTokenLabel])
				#currentLikelihood *= wordsLikelihood[c][unknownTokenLabel]
				
		# update class if greater likelihood is found
		if currentLikelihood > maxLikelihood:
			maxLikelihood = currentLikelihood
			classification = c
	
	return classification

def computeWordsLikelihood(wordsFrequency, numberOfWords, vocabularyLength):
	"""Compute the conditional probability of each word given the class - P(w|c)"""
	likelihood = {}
	for c, words in list(wordsFrequency.items()):
		likelihood[c] = {}
		
		# for each class add likelihood for unknown tokens
		likelihood[c][unknownTokenLabel] = float(1) / (numberOfWords[c] + vocabularyLength + 1)
		for w in words:
			likelihood[c][w] = (words[w] + 1) / (numberOfWords[c] + float(vocabularyLength) + 1)

	return likelihood

def getNumberOfWordsPerClass(wordsFrequency):
	"""Returns the number of ocurrences of words in each class"""
	numberOfWords = {}
	for c, words in list(wordsFrequency.items()):
		numberOfWords[c] = 0
		for w in words:
			numberOfWords[c] += words[w]

		#print('num_' + c + '_words:', numberOfWords[c])

	return numberOfWords

def getNumberOfDocuments(trainData):
	"""Returns the number of documents in te training set"""
	return sum(len(samples) for samples in list(trainData.values()))

def getWordsFrequencyPerClass(trainData, dataDir):
	"""Returns frequency of words in each class"""
	wordsFrequency = {}
	for directory, fileList in list(trainData.items()):
		wordsFrequency[directory] = {} # initialize a dictionary for each class
		for fileName in fileList:
			words = tokenize(open(dataDir + '/' + directory + '/' + fileName).read())
			updateFrequencyDistribution(words, wordsFrequency[directory])
		
	return wordsFrequency	

def getVocabulary(trainData, dataDir):
	"""Returns global vocabulary (unique words) as a list"""
	bagOfWords = []
	for directory, fileList in list(trainData.items()):
		for fileName in fileList:
			bagOfWords += tokenize(open(dataDir + '/' + directory + '/' + fileName).read())	
	return set(bagOfWords)

def computePriors(trainData, numberOfDocs):
	"""Returns a dictionary containing priors for each class in trainData"""
	priors = {}
	for c, data in list(trainData.items()):
		priors[c] = len(data)/float(numberOfDocs)
		
	return priors

def tokenize(text):
	"""Returns unique tokens and bi-grams"""
	
	# split by whitespaces
	tokens = text.strip().split()	
	
	# generate bi-grams
	for i in range(len(tokens)-1):
		tokens += tokens[i] + ' ' + tokens[i + 1]

	# remove duplicate tokens and bi-grams
	tokens = set(tokens)
	
	return tokens

def updateFrequencyDistribution(tokens, dictionary):
	"""Increase frequency for each token in the given dictionary"""
	for t in tokens:
		if t in dictionary:
			dictionary[t] += 1
		else:
			dictionary[t] = 1

def vocabulary(tokens):
	return set(tokens)

def getTrainTestData(dataDir):
	"""Returns two dictionaries (train and test data) with classes as keys and list of samples as values"""
	import os, random
	classes = os.listdir(dataDir)
	trainData = {}
	testData = {}
	
	for c in classes: # directory represents each class for documents		
		# list all documents inside each class
		files = os.listdir(dataDir + '/' + c)		
		# shuffle documents
		fileNames = [fileName for fileName in files]		
		random.shuffle(fileNames)

		trainingCount =int((len(fileNames) * trainingSetPercentage) / 100)

		trainData[c] = [fileName for fileName in fileNames[:trainingCount]]
		testData[c] = [fileName for fileName in fileNames[trainingCount:]]
		
		print('num_' + c + '_training_docs:', len(trainData[c]))
		print('num_' + c + '_test_docs:', len(testData[c]))
		
	return trainData, testData
    
if __name__ == '__main__':
	main()
