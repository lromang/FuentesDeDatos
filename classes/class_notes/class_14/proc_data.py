import os
import pandas as pd
import numpy as np
from argparse import ArgumentParser

class DataProc:

    def __init__(self,  dataset, date_cols, index_col=None,  home_dir='.', data_path='data'):
        self.home_dir = home_dir
        self.data_path = os.path.join(self.home_dir, data_path, f'{dataset}.csv')
        self.date_cols = date_cols
        self.index_col = index_col

    def load_data(self):
        print('Reading dataset')
        try:
            self.data = pd.read_csv(self.data_path,
                                    index_col=self.index_col,
                                    parse_dates=self.date_cols,
                                    date_parser=lambda x: pd.to_datetime(x, infer_datetime_format=True))
            print('Success')
            print(self.data.head())
            print(self.data.dtypes)
        except OSError as e:
            print('Unable to read file')



    def std_cols(self, columns):
        '''
        Standardize the columns of a dataset.
        :param columns: the columns to be standardized.
        :return:
        '''
        self.data[columns] = ((self.data[columns] - self.data[columns].mean(axis=0))
                              .div(self.data[columns].std(axis=0)))

    def gen_index(self, index_col, columns):
        '''

        :param index_col:
        :param columns:
        :return:
        '''
        self.data = self.data.assign(index_col = self.data[columns].mean(axis=1))


    def nan_impute(self, imput_cols, method, by_cat=None):
        '''

        :param imput_cols:
        :param method:
        :param by_cat:
        :return:
        '''
        self.data = (self.data
         .pipe(lambda df: df.fillna(df
                                    .groupby(by_cat)
                                             [imput_cols]
                                    .transform(method))))


if __name__ == '__main__':
    # Instantiate parser
    parser = ArgumentParser()
    parser.add_argument('--dataset', help='The dataset you want to analyze.')
    parser.add_argument('--datecols', help='Date columns to parse separated by comma if any.')
    parser.add_argument('--indexcol', help='Index col if any')
    # Get arguments
    args = parser.parse_args()
    dataset = args.dataset
    date_cols = args.datecols.split(',') if args.datecols else None
    index_col = args.indexcol
    # Read in data
    dp = DataProc(dataset, date_cols, index_col)
    dp.load_data()

    exit

''''data.loc[(data
 .select_dtypes('number')
 .dropna()
 .drop('top_article', axis=1)
 .pipe(lambda df: (df - df.mean(axis=0))/df.std(axis=0))
 .assign(engage_index=lambda df: df.mean(axis=1))).engage_index.idxmax()]




np.random.seed(123454321)

test_data = (pd.DataFrame({'keys': ('a,'*4 + 'b,'*3 + 'c,'*2 + 'd,'+ 'e').split(',')})
 .pipe(lambda df: df.assign(vals1 = np.random.choice([1, 2, 10, np.nan], df.shape[0])))
 .pipe(lambda df: df.assign(vals2 = np.random.randint(0, 10, df.shape[0])))
 .pipe(lambda df: df.assign(vals3 = np.random.randint(50, 100, df.shape[0])))
 .pipe(lambda df: df.assign(vals4 = [f'some text {i}' for i in range(df.shape[0])]))
 )

'''