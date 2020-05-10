from Processor import TextProcessor
from Processor import FileProcessor
from Model import NaiveBayesClassifier

TRAIN_DOCUMENTS = "dataset/train/"
TEST_DOCUMEMENTS = "dataset/test/"
VOCABULARY_DOCUMENT = "results/model.txt"
RESULT_DOCUMENT = "results/result.txt"

class Console:
    def log(self, text):
        print(str(text)+"...")
'''
main method to execute scripts
'''
def main():
    console = Console()
    textProcessor = TextProcessor()
    fileProcessor = FileProcessor()
    
    # load train and test files
    console.log("loading train files")
    trainFiles = fileProcessor.loadDataFiles(TRAIN_DOCUMENTS)
    console.log("loading test files")
    testFiles = fileProcessor.loadDataFiles(TEST_DOCUMEMENTS)
    
    # Process each train documents
    # 1. read a file content into string
    # 2. tokenize the string into words
    # 3. lower each word and counts it frequency
    #    in all class document, in spam class and in ham class document
    # 4. Calculate smoothed conditional probability of each word in class spam and ham
    console.log("processing train documents")
    fileProcessor.processFiles(trainFiles, TRAIN_DOCUMENTS, textProcessor)

    # Build the Vocabulary of words from training documents
    console.log("building vocabulary")
    textProcessor.buildVocabulary()
    # Get the Vocabulary and Store it in a file
    console.log("storing the vocabulary in "+VOCABULARY_DOCUMENT)
    fileProcessor.storeVocabulary(VOCABULARY_DOCUMENT, textProcessor.getVocabulary())

if __name__ == "__main__":
    main()
