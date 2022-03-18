import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import argparse
from utils import *
from Predictor import logit

if __name__ == '__main__':
    # Read size.
    parser = argparse.ArgumentParser()
    parser.add_argument('--size', help='The size of both populations.', type=int)
    # Get size.
    args = parser.parse_args()
    size = args.size
    # Generate random population.
    print(f'Generating population of size: {size}')
    pop = gen_pop()
    # Get values from population.
    X = pop.values[:, 1:]
    y = pop.values[:, 0]
    # Make a forward pass through the logit transformation.
    pred_1 = logit(X, y)
    print(f'Forward pass: {pred_1.forward()}')

