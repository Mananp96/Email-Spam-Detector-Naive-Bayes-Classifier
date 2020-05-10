import re
import os
import math

'''
FileProcessor class for processing email text
'''
class TextProcessor:

    def __init__(self):
        pass
    
    '''
    Tokenize the given text into words
    returns: the array of words
    '''
    def tokenize(self, text):
        return re.split('[^a-zA-Z]', text)

    
'''
FileProcessor class which reads and processes files
'''
class FileProcessor:

    def __init__(self):
        pass
    
    '''
    function to get list of files in a directory
    '''
    def loadDataFiles(self, path):
        return os.listdir(path)
    
    

    
