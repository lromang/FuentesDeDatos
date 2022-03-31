import os
from string import ascii_lowercase as letters
import numpy as np
from pandas.testing import  assert_series_equal
from wordrelatedness import WordRelate
from wrsol import WordRelateSol
from argparse import ArgumentParser
import pickle

class Tester:

    def __init__(self, wr, wr_sol, sw, home_dir='', collection='proj_eval'):
        self.home_dir = home_dir
        self.data_path = os.path.join(self.home_dir, 'data', 'text_comp', 'texts')
        self.collection = collection
        self.wr_sol = wr_sol
        self.wr = wr
        self.sw = sw

    def generate_document(self, n_words=16, line_length=50, n_lines=500, prop_sw=.1):
        MAX_WORDS = 26
        if n_words > MAX_WORDS:
            n_words = MAX_WORDS
            print('Max distinct words: 26. Defaulting to max.')
        if n_words % 2:
            n_words = min(n_words + 1, MAX_WORDS)
            print(f'Number of words must be a multiple of two. Setting nearest valid: {n_words}')
        # Generate population of words
        words = [f'word{letter}' for letter in letters[:n_words]]
        w1 = words[:n_words//2]
        w2 = words[n_words//2:]
        # Probability distribution of words
        n_base = np.arange(n_words//2)
        p2 = np.exp(n_base)/np.sum(np.exp(n_base))
        p1 = p2[::-1]
        # Generate line function
        gen_line = lambda w, p: ' '.join([np.random.choice(w, p=p)
                                 if np.random.rand() < 1-prop_sw else
                                 np.random.choice(self.sw) for _ in range(line_length)])
        # Generate document
        doc = [gen_line(w1, p1) if np.random.rand() < .5 else gen_line(w2, p2) for _ in range(n_lines)]
        # Write document
        with open(os.path.join(self.data_path, self.collection, '000', 'main_text.txt'), 'w') as f:
            f.writelines('\n'.join(doc))

    def test_wr(self, collection, ws=4):
        # Read collection
        max_score = 80
        total_score = []
        print('Checking param initialization')
        if dir(self.wr_sol) == dir(self.wr):
            print('Param initialization passed: 5/5 points')
            total_score.append(5)
        else:
            print('Param initialization failed: 0/5 points')
        print('Checking read_collection')
        self.wr.read_collection(collection)
        self.wr_sol.read_collection(collection)
        if np.array_equal(np.array(self.wr.collections[collection], dtype=object),
                          np.array(self.wr_sol.collections[collection], dtype=object)):
            print('Read collection passed: 15/15 points')
            total_score.append(15)
        else:
            print('Read collection failed: 0/15 points')
        print('Checking get_voc')
        self.wr.get_voc(collection, sw=stopwords)
        self.wr_sol.get_voc(collection, sw=stopwords)
        try:
            assert_series_equal(self.wr.voc[collection], self.wr_sol.voc[collection])
            assert_series_equal(self.wr.ivoc[collection], self.wr_sol.ivoc[collection])
            print('Get voc passed: 10/10 points')
            total_score.append(10)
        except AssertionError:
            print('Get voc failed 0/10 points')
            pass
        print(f'Checking dist_rep ws={ws}')
        self.wr.dist_rep(collection, ws=ws)
        self.wr_sol.dist_rep(collection, ws=ws)
        if np.array_equal(np.array(self.wr.vrm[collection], dtype=object),
                          np.array(self.wr_sol.vrm[collection], dtype=object)):
            print('Distributed representation passed: 35/35 points')
            total_score.append(35)
        else:
            print('Distributed representation failed: 0/35 points')
        print(f'Checking ppmi_reweight')
        self.wr.ppmi_reweight(collection)
        self.wr_sol.ppmi_reweight(collection)
        if np.array_equal(np.array(self.wr.vrm[collection], dtype=object),
                          np.array(self.wr_sol.vrm[collection], dtype=object)):
            print('PPMI reweight passed: 15/15 points')
            total_score.append(15)
        else:
            print('PPMI reweight failed: 0/15 points')
        try:
            print('Generating plot')
            self.wr.dim_redux(collection)
            self.wr.plot_reps()
        except:
            print('Plot not succesfull')
        print(f'Total score: {sum(total_score)}/{max_score}')


if __name__ == '__main__':
    # Check available collections
    collections = os.listdir(os.path.join('data', 'text_comp', 'texts'))
    sw_path = os.path.join('data', 'stop_words', 'stopwords.txt')
    # Parse arguments
    parser = ArgumentParser()
    parser.add_argument('--collection',
                        choices=collections)
    args = parser.parse_args()
    # Read stopwords
    with open(sw_path) as f:
        stopwords = f.read().split('\n')
    # Instantiate WordRelate object
    wr = WordRelate()
    wr_sol = WordRelateSol()
    # Generate document
    collection = args.collection
    # Instantiate tester
    t = Tester(wr, wr_sol, stopwords)
    if collection == 'proj_eval':
        print('Generating new test document')
        t.generate_document()
    # Checking with window size of four
    t.test_wr(collection, ws=4)






