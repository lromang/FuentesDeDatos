import pandas as pd
import numpy as np

data = pd.read_csv('./data/articles_data.csv',
                   index_col=0,
                   parse_dates=['published_at'],
                   date_parser=lambda x: pd.to_datetime(x,
                                                        infer_datetime_format=True))


data.loc[(data
 .select_dtypes('number')
 .dropna()
 .drop('top_article', axis=1)
 .pipe(lambda df: (df - df.mean(axis=0))/df.std(axis=0))
 .assign(engage_index=lambda df: df.mean(axis=1))).engage_index.idxmax()]