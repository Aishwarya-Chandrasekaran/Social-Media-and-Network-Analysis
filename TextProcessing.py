import re

# Class used to pre-process Reddit posts. 
class TextProcessing:
    def __init__(self, tokeniser, lStopwords):
        """
        Initialise the tokeniser and set of stopwords to use.
        """
        self.tokeniser = tokeniser
        self.lStopwords = lStopwords
        
    def process(self, text):
        """
        Perform the processing.
        """
        # Converts the given text words all into lowercase
        text = text.lower()
        # Converts the text into tokens and separate it using ","
        tokens = self.tokeniser.tokenize(text)
        # Removes whitespaces in the text
        tokensStripped = [tok.strip() for tok in tokens]
        
        # pattern for digits
        # the list comprehension in return statement essentially remove all strings of digits or fractions, e.g., 6.15
        regexDigit = re.compile("^\d+\s|\s\d+\s|\s\d+$")
        
        # regex pattern for http
        regexHttp = re.compile("^http")
        
        return [tok for tok in tokensStripped
            if tok not in self.lStopwords and regexDigit.match(tok) is None and regexHttp.match(tok) is None]