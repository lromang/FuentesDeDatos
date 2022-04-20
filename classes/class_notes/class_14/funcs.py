import pandas as pd
import numpy as np

# Read in data with col processing
data = (pd.read_csv('articles_data.csv',
                    index_col=0,
                    parse_dates=['published_at'],
                    date_parser=lambda x: pd.to_datetime(x, infer_datetime_format=True)))

# Getting mean engagment per mont and source
data.filter(regex=r'(source_id|.*published.*|.*_count$)')

(data
 .groupby(['source_id', pd.Grouper(key='published_at', freq='W')])
 .engagement_share_count.mean()))

data.groupby(['source_id', pd.Grouper(key='published_at', freq='M')]).content.agg(list)

(data[~data.content.isna()]
.assign(content=lambda df: df.content.str.split())
.groupby(['source_id', pd.Grouper(key='published_at', freq='M')])
.agg(list).reset_index()
.assign(words = lambda df: df.content.map(lambda x: [y for z in x for y in z])))

#
test_data = pd.DataFrame({'keys': ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'c', 'c'],
                          'v1': [1, 2, np.nan, 3, 40, np.nan, 50, 100, np.nan],
                          'v2': [5, 6, 7, np.nan, 10, 10, np.nan, 5, 5]})

# Fillna with custom function
(test_data
.fillna(test_data.groupby('keys')
        .transform(lambda df: df.median(skipna=True))))

(test_data
.fillna(test_data.groupby('keys').transform(lambda df: df.mean(skipna=True)))
.assign(p_rank = lambda df: df.groupby('keys').v1.rank(ascending=False, pct=True)))

(test_data
.fillna(test_data.groupby('keys')
        .transform(lambda df: df.mean(skipna=True)))
    .assign(p_rank = lambda df: df.groupby('keys').v1.rank(ascending=False, pct=True))
    .assign(lag_v1 = lambda df: df.groupby('keys').v1.shift(1))
    .pipe(lambda df: df.assign(pct_change = lambda df:  (df.v1 - df.lag_v1).div(df.lag_v1))))

