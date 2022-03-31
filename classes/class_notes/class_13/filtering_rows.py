import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', help='The dataset to be analized.', default='movie')
    args = parser.parse_args()
    dataset = args.dataset
    # Data analysis
    movies = pd.read_csv(f'./data/{dataset}.csv')
    # Remember some of the advantages of having a sorted or unique index:
    # - with a sorted index searching for an entry has a time complexity of O(log(n))
    # - with a unique index searching for an entry has a time complexity of O(0)
    #   i.e. constant access time, due to the advantages of hashing.
    movies = movies.set_index('movie_title').sort_index()
    print(f'Index is monotonic: {movies.index.is_monotonic}')
    # Some other advantages come from the fact that with a sorted index
    # we have partial lexicographical matching.
    # 1.- Retrieve all the movies with titles starting with
    #     C to F
    print(movies.loc['C':'F'].head())
    # It is not always convenient to use index based filters
    # particularly if you want to include multiple conditions
    # over several columns.
    # 2.- Filter all movies that have more than 100 critics and
    #     a imdb_score above 8
    print(movies
          .loc[movies.num_critic_for_reviews.gt(100) &
               movies.imdb_score.gt(8)])
    # There are a lot of built in functions that enable us to check for
    # complex conditions such as interval checking or if a value is contained within a list.
    # 3.- Get all the movies that were produced in France, Germany, Canada and have a duration
    # between 2 and 3 hours.
    print(movies
          .loc[movies.country.isin(['France', 'Germany', 'Canada']) &
               movies.duration.between(120, 180)].head())
    # We can also make use of the broadcasting to take advantage of numpy or pandas builtin functions.
    # 4.- Get all the movies that are more than two standard deviations away from the average
    #     number of facebook likes.
    print(movies
          .loc[np.abs(movies.cast_total_facebook_likes -
                      movies.cast_total_facebook_likes.mean())
          .gt(2*movies.cast_total_facebook_likes.std()),
          ['director_name', 'num_critic_for_reviews', 'cast_total_facebook_likes']]
          .sort_values('cast_total_facebook_likes', ascending=False))
    # Stringlike columns have the str suite of methods
    # 5.- Get all the movies where the Director's name has a 'J' in both her first and last name.
    print(movies
          .director_name[movies.director_name.str.lower()
          .str.strip()
          .str.match(r'([^ ]*j[^ ] ?){2,}').fillna(False)])


