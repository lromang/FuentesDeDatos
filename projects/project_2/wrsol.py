import os
import re
import gzip
import magic
import numpy as np
import pandas as pd
import json
from argparse import ArgumentParser
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from scipy import spatial



class WordRelateSol:
    """
    This class implements all the necessary functionality
    to perform similarity analysis between words using distributed representations.
    """

    def __init__(self, home_dir='.'):
        self.home_dir = home_dir
        self.data_path = os.path.join(self.home_dir, 'data', 'text_comp', 'texts')
        self.fig_path = os.path.join(self.home_dir, 'figs')
        # -----------------------------------
        # We'll store all our results at a collection based level i.e.
        # we are going to access every structure within the class
        # using the collection id as keys.
        # TODO
        # Initialize the values (empty dics) for
        # - voc
        # - ivoc
        # - collections
        # - vrm
        # - reduced_vrm
        # (5 points)
        # -----------------------------------
        self.voc, self.ivoc, self.collections, self.vrm, self.reduced_vrm = {}, {}, {}, {}, {}
        print(f"Files found in storage: \n {os.listdir(self.data_path)}")


    def proc_line(self, line):
        '''
        This function parses each input line:
        - sets every word into lowercase
        - remove non words
        - remove empty lines
        - returns a list of words.
        :param line: the line to process
        :return: processed line
        '''
        # -----------------------------------
        # TODO
        # complete the parsers, currently, each word
        # line is outputed as it is.
        # (10 points)
        # -----------------------------------
        return [y for y in [re.sub(r'[^A-Za-z ]+', '', x.lower()) for x in line.split() if x] if len(y) > 0]


    def get_voc(self, collection_id, sw, top_freq_words=2000):
        '''
        Get a series with the most common words in the collection.

        :param collection_id: the id of the collection to process
        :param sw: list of stop words
        :param freq_words: maximum number of words to include in output
        :return:
            - self.voc: a series containing the vocabulary: {word: index},
            - self.ivoc: a series containgin the vocabulary: {index: word} (this will be handy for word retrieval)
        '''
        # -----------------------------------
        # TODO
        # Parse the texts in the collection and
        # build a series with the top_freq_words.
        # Sort the index of voc based on the words.
        # Sort the index of ivoc based on the numerical value.
        # (10 points)
        # -----------------------------------
        voc = pd.Series([word for text in self.collections[collection_id] for word in text if word not in sw]).value_counts()
        voc = voc[:top_freq_words]
        # Obtener palabras con mas frecuencia
        # Make order monotonic to improve performance.
        self.voc[collection_id] = pd.Series(range(len(voc)), index=voc.index).sort_index()
        # Get inverse index for word vocs
        self.ivoc[collection_id] = pd.Series(self.voc[collection_id].index,
                                             index=self.voc[collection_id].values).sort_index()
        print(f'Monotonic index:{self.voc[collection_id].index.is_monotonic}')


    def dist_rep(self, collection_id, ws=4):
        '''
        In this function we get the distributed representation of words based on
        cooccurrence along windows of size ws. This is the most
        challenging question in the project.
        Check https://aclanthology.org/W14-1503.pdf for best practices on this methodology.
        :param collection_id:
        :param ws: size of the context window
        :return:
         - self.vrm: a vectorized representation of the words
        '''
        voc_size = len(self.voc[collection_id])
        self.vrm[collection_id] = np.zeros((voc_size, voc_size))
        for text in self.collections[collection_id]:
            text = np.array([w for w in text if w in self.voc[collection_id]], dtype=object)
            # -----------------------------------
            # TODO
            # For each word in text, build a window
            # of size 2*ws. Containing the vocabulary indexes of ws words prior to the word
            # of interest and ws words after. For example
            # test = [START this is very a simple example]
            # w = this
            # the output window should contain the indexes of the words
            # START, is, very, a, simple.
            # Be sure to structure your output as follows:
            # (iw_c, (iw_in1, iw_in2, ..., iw_inN), (cw_in1, cw_in2, ..., cw_inN))
            # where
            # - iw_c: is the voc index of the central word of the window
            # - iw_ini: is the voc index of the i'th word in the window
            # - cw_ini: is the number of times w_ini appears in the window
            # (35 points)
            # Compare your results with the precomputed matrizes at:
            # ./home_dir/data/tests
            # np.array_equal
            # -----------------------------------
            indexes = [(self.voc[collection_id][w],
                        np.unique(self.voc[collection_id][text[list(range(max(0, i - ws), i)) +
                                                               list(range(i+1, min(i + (ws + 1), len(text))))]].values,
                                  return_counts=True))
                       for i, w in enumerate(text)]
            for word, (related, values) in indexes:
                # -----------------------------------
                # TODO
                # Update the count values in self.vrm.
                # (10 points)
                # -----------------------------------
                self.vrm[collection_id][word, related] += values


    def ppmi_reweight(self, collection_id):
        '''
        In this section we apply ppmi transformation to vrm
        '''
        # -----------------------------------
        # TODO
        # Compute the matrix of expected counts to
        # update vrm.
        # expected_i_j = (row_sum_i*col_sum_j)/tot_sum
        # (15 points)
        # -----------------------------------
        sum_rows = self.vrm[collection_id].sum(axis=1, keepdims=True)
        sum_cols = self.vrm[collection_id].sum(axis=0, keepdims=True)
        sum_tot = self.vrm[collection_id].sum()
        expected = np.dot(sum_rows, sum_cols)/sum_tot
        with np.errstate(divide='ignore'):
            log_vals = np.log(self.vrm[collection_id]/expected)
        self.vrm[collection_id] = np.maximum(log_vals, 0)


    def dim_redux(self, collection_id, dim_reducer='pca'):
        '''
        Apply dimensionality reduction
        :return:
        '''
        if dim_reducer == 'tsne':
            self.reduced_vrm[collection_id] = TSNE(n_components=2,
                                                   init='random').fit_transform(self.vrm[collection_id])
        if dim_reducer == 'pca':
            self.reduced_vrm[collection_id] = PCA(n_components=2).fit_transform(self.vrm[collection_id])


    def plot_reps(self):
        '''
        Plots the reduced representations computed for each collection
        :return:
        '''

        if not os.path.isdir(self.fig_path):
            print('Making figure directory')
            os.mkdir(self.fig_path)

        for i, collection in enumerate(self.collections.keys()):
            fig, ax = plt.subplots(figsize=(12, 10))
            x = self.reduced_vrm[collection][:, 0]
            y = self.reduced_vrm[collection][:, 1]
            ax.scatter(x, y)
            for i, txt in enumerate(self.ivoc[collection]):
                ax.annotate(txt, (x[i], y[i]))
            print(f'saving figure {collection}')
            fig.savefig(os.path.join(self.fig_path, f'{collection}.png'))


    def make_bulk_collections(self):
        '''
        Unifies all collections in one single collection with key 'BULK'
        :return:
        '''
        bulk = []
        for i, collection in enumerate(self.collections.keys()):
                bulk += self.collections[collection]
        self.collections['BULK'] = bulk


    def get_word_relatedness(self, collection):
        '''

        :param word_relate_path:
        :return:
        '''
        word_relate_path = os.path.join(self.home_dir, 'data','relatedness', 'wr.csv')
        wr = pd.read_csv(word_relate_path)
        for index, row in wr.iterrows():
            w1 = row.word1
            w2 = row.word2
            s  = row.score
            # Check if words are in voc
            annotated_sim = []
            predicted_sim = []
            print(w1)
            print(w2)
            if (w1 in self.voc[collection]) and (w2 in self.voc[collection]):
                annotated_sim.append(s)
                similarity = spatial.distance.cosine(wc.vrm[collection][wc.voc[collection][w2]],
                                                     wc.vrm[collection][wc.voc[collection][w1]])
                predicted_sim.append(similarity)
        correlation = np.corrcoef(np.array(annotated_sim), np.array(predicted_sim))[0, 1]
        print(f'Found {len(predicted_sim)} words to relate in voc. Pearson Correlation: {correlation}')
        return correlation

    def read_collection(self, collection_id):
        collection_path = os.path.join(self.data_path, collection_id)
        # Read each file in collection
        texts = []
        for file in os.listdir(collection_path):
            file_path = os.path.join(collection_path, file, 'main_text.txt')
            # Take care of gzipped files
            if re.match(r'^gzip', magic.from_file(file_path)):
                with gzip.open(file_path, 'rb') as f:
                    lines = f.read()
            else:
                with open(file_path, encoding="utf-8") as f:
                    # Read lines and process them. (notice we are removing empty lines)
                    lines = f.readlines()
            # -----------------------------------
            # TODO
            # - Call proc line on each line of input
            # - Make sure to add 'START' and 'END' tokens to the start and end of each sentence.
            # - Preserve only non empty lines.
            # (15 points)
            # -----------------------------------
            texts += [['START'] + self.proc_line(l) + ['END'] for l in lines if self.proc_line(l)]
        # Add texts to the collections.
        self.collections[collection_id] = texts


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
    wc = WordRelateSol()
    # Read collection argument
    # collection = args.collection
    collection = args.collection
    # -----------------------------------
    # TO DO
    # -----------------------------------
    # 1.- read collection 00
    # 2.- get vocabularies
    # 3.- generate distributed representations
    # 4.- apply ppmi
    # 5.- apply dimensionality reduction
    # 6.- Plot results
    # Total lines: ~7
    # To test your execution run:
    # ./wordrelatedness --collection '[collection_id]'
    # -----------------------------------
    wc.read_collection(collection)
    wc.get_voc(collection, sw=stopwords)
    wc.dist_rep(collection, ws=3)
    wc.ppmi_reweight(collection)
    wc.dim_redux(collection)
    wc.plot_reps()