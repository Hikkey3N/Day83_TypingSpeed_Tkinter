import re
import random

############################## Handling Text File to Senteces and Unique Words ##############################

class TextBase():
    def __init__(self):
        self.unique_words = []
        self.sentences = []

        # Read the text from the file
        with open("text.txt", "r") as file:
            text = file.read()
            # Split the text into sentences
            self.sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)

            # Get all words from the text
            words = re.findall(r'\b\w+\b', text.lower())

            # Get unique words
            self.unique_words = list(set(words))
    
    def generate_sentence(self):
        random_index = random.randint(0, len(self.sentences))
        return self.sentences[random_index].strip('.')

    def generate_word(self):
        random_index = random.randint(0, len(self.unique_words))
        return self.unique_words[random_index]