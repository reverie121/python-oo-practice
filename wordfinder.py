from random import choice

"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """
    Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("./few_words.txt")
    12 words read
    """

    def __init__ (self, path):
        """Reads file, creates list of words from file and returns number of words read."""
        self.path = path
        self.words = self.make_word_list(path)
        self.print_num_words_read()

    def __repr__(self):
        return f'<WordFinder path="{self.path}">'

    def make_word_list(self, path):
        """Creates a list of words from file."""
        with open(path, 'r') as file:
            words = [line.strip() for line in file]
        return words
    
    def print_num_words_read(self):
        """Returns number of words in WordFinder's list."""
        return print(f'{len(self.words)} words read')

    def random(self):
        return choice(self.words)

class SpecialWordFinder(WordFinder):
    """
     Machine for finding random words from dictionary, discluding empty lines and comment lines beginning with #.

    >>> wf = WordFinder("./few_words.txt")
    7 words read
    """
    
    def __init__(self, path):
        super().__init__(path)
    
    def make_word_list(self, path):
        """Creates a list of words from file, discluding empty lines and comment lines beginning with #."""
        with open(path, 'r') as file:
            words = [line.strip() for line in file if line.strip() and not line.startswith('#')]
        return words
