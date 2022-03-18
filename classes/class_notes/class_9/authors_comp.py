import re
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import string


class author:

    """
    This class implements all the functionality for
    text scrapping, processing and feature extraction.
    """

    def __init__(self, home_dir, author_id=None, stopwords=None):
        '''
        :param home_dir: root folder for current proyect
        :param author_id: the id of the author to extract
        NOTE: Add a books list to store the extracted contents.
        NOTE DESIGN CHOICES: In most functions we use a paragraph
        # transformation. I.e. we considere all the information at paragraph level.
        # wouldn't it be better to performe this operation only once and store the values.
        # Use your bash and python webscrapping techniques to get the book's
        # ids and create a book dictionary with
        # the following structure:
        # {book_id: [paragraph1, paragraph2, ...., paragraphn], book_id_2: [paragraph1, ..]..}
        # It would also be handy to have a dictionary with the structure
        # {book_id1: title1, book_id2: title2, ...}
        # for future references on the titles of each book. (the title should also be provided
        # by your webscrapping routine).
        # - Make sure to intialize self.books as a dict.
        # - Makle sure to initialize self.book_names as a dict.
        '''

        print(':Init Author:')
        self.home_dir = home_dir
        self.author_id = author_id
        self.root_url = 'https://www.gutenberg.org'
        self.text_url = f'{self.root_url}/files'
        self.author_url = f'{self.root_url}/ebooks/author/{self.author_id}'
        self.stopwords = stopwords
        self.books_urls = []
        self.books = []
        self.features = {}

    def get_books(self, n_books=10):
        '''
        :param n_books: number of books to download. (tops at the resource limit)
        :return: al list with all the contents of all the books for this author
        Note the try-catch statement and the proper way to catch an urllib exception.
        '''
        # First get books_urls
        if len(self.books_urls) == 0:
            self.get_books_urls(n_books)

        for book_url in self.books_urls:
            clean_book_url = '{book_url}{extra_zero}.txt'
            try:
                book_format = clean_book_url.format(book_url=book_url,
                                                    extra_zero='')
                print(f'Trying book_format: {book_format}')
                book_connect = urlopen(book_format)
                book_content = BeautifulSoup(book_connect.read(), 'html.parser')
            # Proper way to handle an HTTP exception
            except urllib.error.HTTPError as exception:
                book_format = clean_book_url.format(book_url=book_url,
                                                    extra_zero='-0')
                print(f'Trying book_format: {book_format}')
                book_connect = urlopen(book_format)
                book_content = BeautifulSoup(book_connect.read(), 'html.parser')
            # Do the following only if you know what you are doing. Remember that
            # keyboard interruption is an exception.
            except:
                book_content = None
                pass
            # Add content
            if book_content:
                # Remove special characters!
                self.books.append(re.sub('\r', '', book_content.get_text()))

        print(f'{len(self.books)} books ingested. ')

    def get_books_urls(self, n_books=10):
        '''

        :param n_books: number of books to download. (tops at the resource limit)
        :return: al list with all the contents of all the books for this author
        '''

        url_connect = urlopen(f'{self.author_url}')
        url_content = BeautifulSoup(url_connect.read(), 'html.parser')
        # Split this code, try to understand what each part is doing.
        # The other alternative (reiterative and less flexible, but also instructive) to get book_ids:
        # [f'{text_url}{t}/{t}-0.txt' for t in [re.search(r'([^/])+$', t.find('a').get('href')).group(0)
        # for t in url_content.find_all('li', {'class':'booklink'})]]
        book_ids = [re.search(r'([^/]+)$', x).group(0)
                    for x in [t.get('href') for t
                              in url_content.find_all('a', {'class': 'link'})] if x and
                    re.match(r'.*[0-9]+$', x)]
        # Store values in object
        self.books_urls = [f'{self.text_url}/{book_id}/{book_id}' for book_id in book_ids[:n_books]]
        return self.books_urls

    def make_feature_dict(self):
        '''
        create the object's feature dictionary
        {feature1: [feature1_book1, feature1_book2, ..], feature2: [feature2_book1, feature2_book2]}
        NOTE: this method is highly inefficient
        '''
        self.features = {'mean_paragraph_length': [self.mean_paragraph_length(book) for book in self.books],
                         'mean_sentence_length': [self.mean_sentence_length(book) for book in self.books],
                         'mean_punctuation': [self.mean_punctuation(book) for book in self.books],
                         'mean_unique': [self.mean_unique(book, stopwords=self.stopwords) for book in self.books],
                         'mean_stop': [self.mean_stop(book, stopwords=self.stopwords) for book in self.books]}

    @staticmethod
    def mean_paragraph_length(book):
        '''
        Task: Try this function with this input:
        book = 'this.is.a.paragraph.\n\n'*2 +  'this.is.another.paragraph.'*2 + 'endofbook.'
        make sure you understand what it is doing
        :return: The average number of words per paragraph. '\n\n'
        '''

        paragraphs = book.split('\n\n')
        return sum([len(re.findall(r'\w+', paragraph)) for paragraph in paragraphs])/len(paragraphs)

    @staticmethod
    def mean_punctuation(book):
        '''
        Task: Try this function with this input:
        book = 'this.is.a.paragraph.\n\n'*2 +  'this.is.another.paragraph.'*2 + 'endofbook.'
        make sure you understand what it is doing
        :return: The average number of punctuation characters per paragraph. 'string.punctuation'
        '''

        punct = string.punctuation
        paragraphs = book.split('\n\n')
        return sum([len(re.findall(rf'[{punct}]', paragraph)) for paragraph in paragraphs])/len(paragraphs)

    @staticmethod
    def mean_sentence_length(book):
        '''

        :return: The average number of words per sentence. split('.')
        '''
        sentences = [x for x in book.split('.') if x]
        return sum([len(re.findall(r'\w+', sentence)) for sentence in sentences])/len(sentences)

    @staticmethod
    def mean_unique(book, stopwords):
        '''
        This one is somewhat tricky, make sure you understand what each
        component is doing. USE THIS EXAMPLE
        book = 'this.is.a.paragraph.\n\n'*2 +  'this.is.another.paragraph.'*2 + 'endofbook.'
        :return: The average number of unique non-stop words per sentence.
        '''

        paragraphs = book.split('\n\n')
        return sum([len(set(y) - set(stopwords))
                    for y in [[line for line in re.sub(r'.$', '', paragraph).split('.')]
                              for paragraph in paragraphs]])/len(paragraphs)

    @staticmethod
    def mean_stop(book, stopwords):
        '''

        :return: The average number of stopwords per sentence.
        '''
        sentences = [x for x in book.split('.') if x]
        return sum([len([word for word in sentence if word in stopwords]) for sentence in sentences])/len(sentences)