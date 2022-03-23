import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def gen_pop(size=100, seed=123454321):

    '''
    This function generates a random population of a given size.
    :param size: The size of the population.
    :param seed: A random seed for reproducibility.
    :return:
    '''
    # Generate random sample.
    np.random.seed(seed)
    # Generate first random population
    # This is a multivariate normal. We need an array of means and a covariance matrix.
    # - TODO:
    # Try different visualizations using a covarianze matrix for independent variables.
    # and genrating each population separately with np.random.normal.
    # Hint:
    # generate two independent normal distributions (reshape them) and use hstack.
    # Hint:
    # To visualize you just need to call the function viz_pop(pop)
    # with the new population.
    pop1 = np.random.multivariate_normal(mean=np.array([5, 10]),
                                         cov=np.array([[1, .5], [.5, 1]]),
                                         size=size)
    # Generate second random population.
    pop2 = np.random.multivariate_normal(mean=np.array([10, 5]),
                                         cov=np.array([[1, .5], [.5, 1]]),
                                         size=size)
    # Stack populations.
    pop = np.vstack((pop1, pop2))
    # Generate labels.
    labels = np.vstack((np.ones(size).reshape(-1, 1), np.zeros(size).reshape(-1, 1)))
    # Returning a dataframe for convenience.
    return pd.DataFrame(np.hstack((labels, pop)), columns=['label', 'x1', 'x2'])


def viz_pop(pop):
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.scatterplot(x='x1', y='x2', hue='label', data=pop, ax=ax)
    fig.savefig('test_pop.png')
