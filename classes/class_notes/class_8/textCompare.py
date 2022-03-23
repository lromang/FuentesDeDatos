import os
import re
from functools import reduce

class TextCompare:

    """
    This class parses a text
    """

    def __init__(self, home_dir='.'):
        self.home_dir = home_dir
        self.collection = {}
        self.mean_sent_len = {}
        self.n_paragraphs = {}

    def list_files(self):
        print(os.listdir(self.home_dir))

    def read_file(self, file_name):
        # parsed_name = re.sub(r'\.[^\.]+$', '', file_name)
        with open(os.path.join(self.home_dir, f'{file_name}.txt')) as f:
            self.collection[file_name] = f.read()

    def get_paragraphs(self, file_name):
        self.n_paragraphs[file_name] = len(self.collection[file_name].split('\n\n'))

    def get_mean_length_sentence(self, file_name):
        text = self.collection[file_name]
        sent_len = [len(s.split()) for s in text.split('.')]
        return reduce(lambda x, acc: x + acc, sent_len)/len(sent_len)

if __name__ == '__main__':
    file_name = 'main_text'
    tc1 = TextCompare()
    print('READ FILE')
    tc1.read_file(file_name)
    print('FILE INSIDE MEAN LENGTH')
    print(tc1.get_mean_length_sentence(file_name))