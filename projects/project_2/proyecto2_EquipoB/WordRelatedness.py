#! PATH/TO/ENVIRONMENT/BIN PYTHON

import os
import re
import gzip
#import magic
import numpy as np

import pandas as pd
from argparse import ArgumentParser
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from scipy import spatial

class WordRelate:
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
        self.voc={}
        self.ivoc={}
        self.collections={}
        self.vrm={}
        self.vrmlog={}
        self.reduced_vrm={} 
        print(f"Files found in storage: \n {os.listdir(self.data_path)}")
    
    def proc_line(self, line):
    	parsed_lines = [x for x in re.sub(r'[^a-zA-Z\s]', '',line).lower().split()] 
    	return parsed_lines
        
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
        # Your code goes here (~ 2 lines)
        
        
        text=self.read_collection(collection_id)
        words=[word for word in text if word not in sw]
        a=pd.value_counts(words).index
        # Make order monotonic to improve performance.
        self.voc=dict(zip(a,[x for x in range(len(a))]))
        # Get inverse index for word vocs
        self.ivoc=dict((v,k)for k,v in self.voc.items())
        #print(f'Monotonic index:{self.voc[collection_id].index.is_monotonic}')
        
    def dist_rep(self, collection_id,sw, ws=4):
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
        
        #for text in self.collections[collection_id]:
        #	print(self.collections[collection_id])
        #    text = np.array([w for w in text if w in self.voc[collection_id]], dtype=object)
        #    print(text)
        text=self.read_collection(collection_id)
        text=[word for word in text if word not in sw]
        self.get_voc(collection_id,sw)
        voc_size = len(self.voc)
        self.vrm[collection_id] = np.zeros((voc_size, voc_size))
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
		
        ventanas=pd.DataFrame(columns=['centro','vi4','vi3','vi2','vi1','vd1','vd2','vd3','vd4'])
        for i in range(ws,len(text)-ws): 
        	centro=self.voc[text[i]]
        	a=[]
        	a.append(centro)
        	for h in range (i-ws,i+ws+1): 
        		if h!=i:
        			a.append(self.voc[text[h]])#posiciones en el voc 
        	df=pd.DataFrame([a],columns=['centro','vi4','vi3','vi2','vi1','vd1','vd2','vd3','vd4'])
        	ventanas=ventanas.append(df,ignore_index=True)
            
        
        
        for i in range(voc_size):
            v=ventanas.loc[ventanas['centro']==i]
            for j in range(voc_size):
                if (len(v)>0):
                    rep=0
                    for k in range(len(v)):
                        for l in ventanas.columns.values[1:2*ws]:
                            val=(v.loc[[v.index.values[k]],[l]]).iat[0,0]#valor
                            if (val==j):
                                rep=rep+1
                    self.vrm[collection_id][i][j]=rep#i=centro, j=palabras en la ventana 
                else:
                    self.vrm[collection_id][i][j]=0
        vrmdf=pd.DataFrame(self.vrm[collection_id],columns=self.voc.keys(),index=self.voc.keys())
        print(vrmdf)

            #for word, (related, values) in indexes:
                # -----------------------------------
                # TODO
                # Update the count values in self.vrm.
                # (10 points)
                # -----------------------------------

                # Your code goes here (1 line)


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

        r=self.vrm[collection_id].sum(axis=1)
        c=self.vrm[collection_id].sum(axis=0)
        t=self.vrm[collection_id].sum()
        M = np.zeros((len(self.vrm[collection_id]), len(self.vrm[collection_id])))
        for i in range(len(self.vrm[collection_id])): 
            for j in range(len(self.vrm[collection_id])): 
                M[i][j]=(r[i]*c[j])/t


    def dim_redux(self, collection_id, dim_reducer='pca'):
        '''
        Apply dimensionality reduction
        :return:
        '''
        if dim_reducer == 'tsne':
            self.reduced_vrm[collection_id] = TSNE(n_components=2,
                                                   init='random').fit_transform(self.vrm[collection_id])
        if dim_reducer == 'pca':
            
            try:
                self.reduced_vrm[collection_id] = PCA(n_components=2).fit_transform(self.vrm[collection_id])
            except(ValueError):
                print("error en dim redux")
                pass

    def plot_reps(self):
        '''
        Plots the reduced representations computed for each collection
        :return:
        '''

        if not os.path.isdir(self.fig_path):
            print('Making figure directory')
            os.mkdir(self.fig_path)
        
        try:
            for i, collection in enumerate(self.collections.keys()):
                fig, ax = plt.subplots(figsize=(12, 10))
                x = self.reduced_vrm[collection][:, 0]
                y = self.reduced_vrm[collection][:, 1]
                ax.scatter(x, y)
                print("1st for works")
                for i, txt in enumerate(self.ivoc):
                    ax.annotate(txt, (x[i], y[i]))
                print(f'saving figure {collection}')
                fig.savefig(os.path.join(self.fig_path, f'{collection}.png'))
        except(KeyError):
            print("error en plot reps")
            pass


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
            #if re.match(r'^gzip', magic.from_file(file_path)):
             #   with gzip.open(file_path, 'rb') as f:
              #      lines = f.read()
            #else:
            with open(file_path, encoding="utf-8") as f:
                    # Read lines and process them. (notice we are removing empty lines)
                lines = f.readlines()
            for line in lines:
            	if line:
            		l=self.proc_line(line)
            		l.insert(0,"START")
            		l.insert(len(l),"END")
            		texts.extend(l) 
    

        # Add texts to the collections.
        self.collections[collection_id] = texts
        return self.collections[collection_id]


if __name__ == '__main__':
    # Check available collections
    collections = os.listdir(os.path.join('data', 'text_comp', 'texts'))
    # Parse arguments
    parser = ArgumentParser()
    parser.add_argument('--collection',
                        choices=collections)
    args = parser.parse_args()
    # Read stopwords
    with open('./data/stop_words/stopwords.txt') as f:
        stopwords = f.read().split('\n')
    # Instantiate WordRelate object
    wc = WordRelate()
    # Read collection argument
    collection = args.collection
    wc.read_collection('01')
    wc.get_voc('01',stopwords)
    wc.dist_rep('01',stopwords)
    wc.ppmi_reweight('01')
    wc.dim_redux('01')
    wc.plot_reps()
    
     # -----------------------------------
    # TO DO
    # -----------------------------------
    # 1.- read collection 00
    # 2.- get vocabularies
    # 3.- generate distributed representations
    # 4.- apply ppmi
    # 5.- apply dimensionality reduction
    # 6.- Plot results
    # To test your execution run:
    # ./wordrelatedness --collection '[collection_id]'
    # Your final output should produce two plots
    # such as the one displayed in:
    # ./home_dir/figs/.
    # -----------------------------------
    
    
