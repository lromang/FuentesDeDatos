import re
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup

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
        self.text_url = f'{self.root_url}/files'
        self.author_url = f'{self.root_url}/ebooks/author/{self.author_id}'
        self.books_urls = []
        self.books = []


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
        Note the try-catch statement and the proper way to catch an urllib exception.
        '''

        for book_url in self.books_urls:
            clean_book_url = '{book_url}{extra_zero}.txt'
            try:
                book_format = clean_book_url.format(book_url=book_url,
                                                    extra_zero='')
                print(f'Trying book_format: {book_format}')
                book_connect = urlopen(book_format)
                book_content = BeautifulSoup(book_connect.read(), 'html.parser')
                self.books.append(book_content.get_text())
            # Proper way to handle an HTTP exception
            except urllib.error.HTTPError as exception:
                book_format = clean_book_url.format(book_url=book_url,
                                                    extra_zero='-0')
                print(f'Trying book_format: {book_format}')
                book_connect = urlopen(book_format)
                book_content = BeautifulSoup(book_connect.read(), 'html.parser')
                self.books.append(book_content.get_text())
            # Do the following only if you know what you are doing. Remember that
            # keyboard interruption is an exception.
            except:
                pass

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
                              in url_content.find_all('a', {'class': 'link'})] if
                    re.match(r'.*[0-9]+$', x)]
        # Store values in object
        self.books_urls = [f'{self.text_url}/{book_id}/{book_id}' for book_id in book_ids[:n_books]]
        return self.books_urls

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