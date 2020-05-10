import re
import os
import math

'''
FileProcessor class for processing email text
'''
class TextProcessor:

    def __init__(self):
        self.word_frequency = {}
        self.words_Ham = {}
        self.words_Spam = {}
        self.Delta = 0.5
        self.sizeOfHam = 0
        self.sizeOfSpam = 0
        self.sizeOfCorpus = 0
    
    '''
    Tokenize the given text into words
    returns: the array of words
    '''
    def tokenize(self, text):
        return re.split('[^a-zA-Z]', text)

    '''
    Lower the each word and counts the word frequency in 
    all documents and store it in word_frequency

    e.g {word: count}
    '''
    def recordWordCount(self, words):
        for word in words:
            if word != '':
                if word.lower() in self.word_frequency:
                    self.word_frequency[word.lower()] += 1
                else:
                    self.word_frequency[word.lower()] = 1
    
    '''
    Returns the unique words from document
    '''
    def getWordsFromDocument(self, words):
        wordsList = []
        for word in words:
            if word != '':
                wordsList.append(word.lower())
        return wordsList

    '''
    Calculate Frequency Of Word in a class
    where classType: (spam|ham)
    '''
    def updatefrequencyCountInClass(self, classType, words):
        for word in words:
            if word != '':
                if(classType == 'ham'):
                    if word.lower() in self.words_Ham:
                        self.words_Ham[word.lower()] += 1
                    else:
                        self.words_Ham[word.lower()] = 1
                        
                if(classType == 'spam'):
                    if word.lower() in self.words_Spam:
                        self.words_Spam[word.lower()] += 1
                    else:
                        self.words_Spam[word.lower()] = 1
    
    '''
    returns smoothed conditional probability of words against classType
    where classType: (spam|ham)
    smoothed conditional Probabilty = P(word | classType)

                                                (frequency of word in class) + delta
    where; P(word | class) = ____________________________________________________________________________
                                (total number of words in class) + delta * (size of vocabulary or corpus)
    '''
    def calculateCondProb(self, frequency, classType):
        freqWord = 0
        sizeOfCorpus = self.sizeOfCorpus
        freqWord = frequency

        if(classType == 'ham'):
            totalNoOfWords = self.sizeOfHam
        else:
            totalNoOfWords = self.sizeOfSpam
        
        prob = ( (freqWord + self.Delta) / (totalNoOfWords + (self.Delta * sizeOfCorpus)) )
        return prob
    
    '''
    Returns the frequency of word in all documents
    
    e.g word_frequency = {word : count}
    '''
    def getWordFrequency(self):
        return self.word_frequency

    '''
    Returns the frequency of word in class Ham
    
    e.g words_Ham = {word : count}
    '''
    def getWordsHam(self):
        return self.words_Ham
    
    '''
    Returns the frequency of word in class Spam
    
    e.g words_Spam = {word : count}
    '''
    def getWordsSpam(self):
        return self.words_Spam
    
'''
FileProcessor class which reads and processes files
'''
class FileProcessor:

    def __init__(self):
        self.space = "  "
    
    '''
    function to get list of files in a directory
    '''
    def loadDataFiles(self, path):
        return os.listdir(path)

    '''
    Returns the file name
    '''
    def getDocumentName(self, file):
        docBase = os.path.basename(file.__getattribute__('name'))
        docName = os.path.splitext(docBase)[0]
        return docName

    '''
    Indentifies the class type (spam | ham) from the file name
    '''
    def getClassType(self, file):
        docName = self.getDocumentName(file)

        if re.search('(.*)-(ham)-(.*)', docName):
            return 'ham'
        else:
            return 'spam'

    '''
    Returns the number of total documents, spam documents and
    ham documents in a directory
    '''
    def getNumOfDocuments(self, files):
        totalDocuments = len(files)
        HamDocuments = 0
        SpamDocuments = 0
        for file in files:
            if re.search('(.*)-(ham)-(.*)', file):
                HamDocuments += 1
            else:
                SpamDocuments += 1    

        return totalDocuments, HamDocuments, SpamDocuments
        
    '''
    read files line by line and processes it from TextProcessor
    '''
    def processFiles(self, files, path, textProcessor):
       
        for file in files:
            try:
                with open(str(path+file), "r", encoding="utf8", errors='ignore') as f:
                    classType = self.getClassType(f)

                    for line in f:
                        line = line.strip()
                        words = textProcessor.tokenize(line)
                        textProcessor.recordWordCount(words)
                        textProcessor.updatefrequencyCountInClass(classType, words)

            finally:
                f.close()
   
    

    
