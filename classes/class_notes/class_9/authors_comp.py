import re

class author:

    """
    This class implements all the functionality for
    text scrapping, processing and feature extraction.
    """

    def __init__(self, home_dir, author_id=None):
        '''
        :param home_dir: root folder for current proyect
        :param author_id: the id of the author to extract
        NOTE: Add a books list to store the extracted contents.
        '''

        self.home_dir = home_dir
        self.author_id = author_id
        self.root_url = 'https://www.gutenberg.org'
        self.text_url = f'{self.root_url}/files/'
        self.author_url = f'{self.root_url}/ebooks/author/{self.author_id}'


    def get_book(self, book_url):
        '''
        This function returns the parsed contents of the specified book_url
        :param book_url: the url of the book to download
        :return: the book contents without special characters
        '''

    def get_books(self, n_books=10):
        '''

        :param n_books: number of books to download. (tops at the resource limit)
        :return: al list with all the contents of all the books for this author
        '''

    def mean_paragraph_length(self):
        '''

        :return: The average number of words per paragraph.
        '''

    def mean_punctuation(self):
        '''

        :return: The average nummber of punctuation characters per paragraph.
        '''

    def mean_sentence_length(self):
        '''

        :return: The average number of words per sentence.
        '''

    def mean_unique(self):
        '''

        :return: The average number of unique non-stop words per sentence.
        '''

    def mean_stop(self):
        '''

        :return: The average number of stopwords per sentence.
        '''

    def say_hello(self):
        print(f"Hello, I'm author: {self.author_id}")