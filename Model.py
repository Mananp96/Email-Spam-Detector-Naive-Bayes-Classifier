import math

SPAM = 'spam'
HAM = 'ham'
WRONG = 'wrong'
RIGHT = 'right'

'''
NaiveBayes classifier
'''
class NaiveBayesClassifier:

    def __init__(self):
        self.PriorH = 0.0
        self.PriorS = 0.0
        self.vocabulary = {}
        self.result = {}

    def getPriorHam(self):
        return self.PriorH
    
    def setPriorHam(self, totalDocuments, hamDocuments):
        self.PriorH = math.log10(hamDocuments / totalDocuments)

    def getPriorSpam(self):
        return self.PriorS
    
    def setPriorSpam(self, totalDocuments, spamDocuments):
        self.PriorS = math.log10(spamDocuments / totalDocuments)

    '''
    fit the vocabulary
    '''
    def fit(self, vocabulary):
        self.vocabulary = vocabulary
    
    '''
    Returns the classification result
    '''
    def getClassificationResult(self):
        return self.result
    

    
        



