import pandas as pd
import numpy as np
import time
import os
from sklearn.decomposition import PCA
from utils import *
from Predictor import Logit

class SentClass:

    def __init__(self, data_path, stopwords):
        '''
        Here we intialize all the required attributes of our class.
        Take notice of the structure of feature_voc since this will be
        relevant latter on.
        :param data_path: the path to the data source.
        :param stopwords: a list of stopwords.
        '''
        self.data_path = data_path
        self.sw = stopwords
        self.voc = None
        self.data = None
        self.model = None
        self.dim_redux = None
        self.feature_voc = {'f0': {'pos': None, 'neg': None},
                            'f1': {'pos': None, 'neg': None},
                            'f2': {'pos': None, 'neg': None},
                            'f3': {'pos': None, 'neg': None}}

    def read_data(self, sent_col, pos_label='positive', neg_label='negative'):
        '''
        This function reads the data and maps string class labels into 1, 0
        :param sent_col: the column that contains the sentiment
        :param pos_label: the string label for the positive class
        :param neg_label: the string label for the negative class
        :return:
        '''
        self.data = (pd.read_csv(os.path.join(self.data_path, 'data.csv'))
                     .assign(clean_sentiment=lambda df: df[sent_col].map({pos_label: 1, neg_label: 0})))

    def clean_text_df(self, text_col):
        '''
        This function applies the proc_text function to text_col within self.data
        and returns the values in a new column with name: words_df
        :param text_col: the column to be cleaned
        '''
        self.data = (self
                     .data
                     .assign(clean_text=lambda df: proc_text_df(df, text_col, self.sw))
                     .rename({'clean_text': f'words_df'}, axis=1))

    def clean_text(self, text_col):
        '''
        This function applies the proc_text function to text_col within self.data
        and returns the values in a new column with name: words
        :param text_col: the column to be cleaned

        TODO

        Apply your implementation of proc_text from utils to text_col (in this case the column of interest is review)
        and store the result in a new column named words in self.data

        [10 points]
        '''
        needed_col = self.data[text_col]
        needed_fun = lambda row : proc_text(row,self.sw)
        self.data['words'] = needed_col.apply(needed_fun)

    def gen_voc(self, min_count=500):
        '''
        This function extracts the vocabulary from the *words* column (the output of clean_text).
        :param min_count: The minimum number of entries the word most have within the corpus.

        TODO

        1.- Generate the vocabulary from *words* column in self.data. as a **SERIES** with ordered
        index. The vocabluary most contain words that have at least *min_count* entries within the corpus.

        2.- Make sure to clean self.data.words (removing the words that are not inside of the vocabulary

        [25 points]
        '''
        query = "count >= " + str(min_count)
        self.voc = self.data.words.value_counts().reset_index(name='count').query(query)["index"]

        # Filter words only those in voc.
        self.data.words = self.data.words.isin(self.voc)

    def gen_voc_features(self, feature_col):
        '''

        This function generates a series of positive and negative entries per feature_col

        :param feature_col: the feature col from which the pos an neg vocabularies are generated
        :return: positive voc of features, negative voc of features.
        '''
        w_counts = (self.data
                    .groupby('sentiment')
                    [feature_col]
                    .apply(list)
                    .map(lambda x: [y for z in x for y in z])
                    .reset_index())
        pos_voc = pd.Series(w_counts.reset_index()[feature_col][0]).value_counts(normalize=True)
        neg_voc = pd.Series(w_counts.reset_index()[feature_col][1]).value_counts(normalize=True)
        return pos_voc, neg_voc

    def build_data_features(self):
        '''
        This function adds three feature columns to self.data:

             - bigrams: a column of bigrams from words
             - neg_words: a column of words with 'neg_' prefixes
             - neg_bigrams: a column of bigrams from neg_words

        TODO

        - Apply get_bigrams to words and assign it to a bigrams column in self.data
        - Apply prefix_neg to words and assign it to a neg_words column in self.data
        - Apply get_bigrams to neg_words and assign it to a neg_bigrams column in self.data

        [10 points]
        '''
        
        self.data['bigrams'] = get_bigrams(self.data.words)
        self.data['neg_words'] = prefix_neg(self.data.words)
        self.data['neg_bigrams'] = get_bigrams(self.data.neg_words)

    def get_feature_voc(self):
        '''
        This function populates feature_voc with features for: words, bigrams, neg_words and neg_bigrams.

        TODO

        Call gen_voc_features for each feature and populate feature_voc.

        [10 points]
        '''
        # Generate data features
        self.build_data_features()
        # Iterate over each feature
        feature_cols = ['words', 'bigrams', 'neg_words', 'neg_bigrams']
        for i, feature in enumerate(feature_cols):
            print(f'Processing feature: {feature}')
            pos, neg = self.gen_voc_features(feature)
            self.feature_voc[f'f{i}']['pos']= pos
            self.feature_voc[f'f{i}']['neg']= neg

    def text_to_features(self, text):
        '''
        This function takes as input a sample text and generates all the necessary features.
        :param text: the text to be processed
        :return: a dataframe with all the textual features
        '''
        features = {'f0_pos': 0, 'f0_neg': 0,
                    'f1_pos': 0, 'f1_neg': 0,
                    'f2_pos': 0, 'f2_neg': 0,
                    'f3_pos': 0, 'f3_neg': 0}
        words = proc_text(text, self.sw)
        neg_words = prefix_neg(words)
        data_features = {'f0': words, 'f1': get_bigrams(words),
                         'f2': neg_words, 'f3': get_bigrams(neg_words)}
        for i in range(4):
            if i in [0,2]:
                features[f'f{i}_pos'] = np.mean([self.feature_voc[f'f{i}']['pos'][w]
                                                 if w in self.feature_voc[f'f{i}']['pos'] else 0
                                                 for w in data_features[f'f{i}']])
                features[f'f{i}_neg'] = np.mean([self.feature_voc[f'f{i}']['neg'][w]
                                                 if w in self.feature_voc[f'f{i}']['neg'] else 0
                                                 for w in data_features[f'f{i}']])
            else:
                features[f'f{i}_pos'] = np.mean([self.feature_voc[f'f{i}']['pos'][tuple(w)]
                                                 if tuple(w) in self.feature_voc[f'f{i}']['pos'] else 0
                                                 for w in data_features[f'f{i}']])
                features[f'f{i}_neg'] = np.mean([self.feature_voc[f'f{i}']['neg'][tuple(w)]
                                                 if tuple(w) in self.feature_voc[f'f{i}']['neg'] else 0
                                                 for w in data_features[f'f{i}']])
        return pd.DataFrame(features, index=[1])

    def create_feature_matrix(self, df, text_col):
        '''
        This function constructs a dataframe of features from a given text_col
        :param df: a data frame to process
        :param text_col: the text_col from which features are extracted
        :return: a feature dataframe
        '''
        feature_df = df[text_col].map(lambda x: self.text_to_features(x))
        return pd.concat(feature_df.values, axis=0)*100

    def predict(self, df, text_col):
        '''
        This function takes as input a new data frame together with a text column to predict sentiment.
        :param df: new dataset
        :param text_col: text column over which predict sentiment
        :return: an array of probabilities of sentiment.
        '''
        X = self.create_feature_matrix(df, text_col)
        X_redux = self.dim_redux.transform(X)
        new_X = np.hstack((np.ones(X_redux.shape[0]).reshape(-1, 1), X_redux)).T
        # Generate predictions and shape them as grid.
        return self.model.forward(new_X)

    def train_model(self, text_col, sent_col):
        '''
        This function trains our model with the given text and sentiment column.
        :param text_col: the column containing the text to be classified
        :param sent_col: the column containing the true sentiment labels
        '''
        print('Creating feature matrix...')
        X = self.create_feature_matrix(self.data, text_col)
        self.dim_redux = PCA(n_components=2).fit(X)
        X_redux = self.dim_redux.transform(X)
        print(X_redux[:10])
        print(self.data[sent_col].values[:10])
        # Instantiate model
        self.model = Logit(X_redux, self.data[sent_col].values)
        # Optmize parameters
        self.model.optimize()
        # Generate classification region plot.
        self.model.plot_region(X_redux)


if __name__ == '__main__':
    # Read in stopwords
    with open('./data/stopwords.txt') as f:
        sw = f.read().split('\n')
    home_dir = '.'
    sc = SentClass(os.path.join(home_dir, 'data'), sw)
    print('Reading data...')
    sc.read_data('sentiment')
    print('Data Read!')
    print('Cleaning Text...')
    sc.clean_text('review')
    print('Text cleaned!')
    print('Gettic voc features...')
    sc.get_feature_voc()
    print('Voc Features Aquired!')
    print('Columns:')
    print(sc.data.columns)
    print('Training model...')
    sc.train_model('review', 'clean_sentiment')
    print('Model trained!')
    print('Bye!')