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
    pop = gen_pop(size)
    # Get values from population.
    X = pop.values[:, 1:]
    y = pop.values[:, 0]
    # Instantiate logit predictor.
    pred_1 = logit(X, y)
    # Optmize parameters
    pred_1.optimize()
    # Generate classification region plot.
    pred_1.plot_region(X)


