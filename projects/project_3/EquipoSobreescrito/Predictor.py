import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Logit:

    """
    This class implements the logit classifier:
    Remember from class:
    We are trying to model the log odds of the
    probability of P(y_i = 1| X) using a linear model
    on X = (x_1 | x_2 |...|x_m). Where x_i, y in R^n.

    In other words, we are opting for the following setup

    log(p_y_i/(1-p_y_i)) = sum_j_n alpha_j*x_ji
    =>
    p_y_i = 1/(1+e^-z_i)
    where
    z_i = sum_j_n alpha_j*x_ji
    """

    def __init__(self, X, y, alpha=.005):
        # Notice the order of the operations
        # first we normalize, then we transpose
        # and finally append ones.
        self.X = np.vstack((np.ones(y.shape), self.normalize(X).T))
        self.y = y.reshape(1, -1)
        self.thetas = np.random.rand(self.X.shape[0]).reshape(1, -1)
        self.alpha = alpha
        self.train = []

    def forward(self, X):
        '''
        Apply phi
        HINT 1: np.dot
        HINT 2: np.exp
        HINT 3: check the shape of theta!
        :return: phi(z)
        '''
        return 1/(1 + np.exp(-1*np.dot(self.thetas, X)))

    def loss(self):
        '''

        :return:
        '''
        y_hat = self.forward(self.X)
        return -1*np.mean(self.y*np.log(y_hat) + (1-self.y)*np.log(1-y_hat))

    def grads(self):
        '''
        dL/dbeta_j = (-1/n sum_i_n (yi-y_h_i)*xij)
        :return:
        '''
        y_hat = self.forward(self.X)
        return -1*np.mean((self.y-y_hat)*self.X, axis=1, keepdims=True)

    def optimize(self, err=.01, Tol=1e4, savefig='error.png'):
        '''

        :return:
        '''
        iter = 0
        loss = self.loss()
        print(loss)
        print('Training')
        while loss > err and iter < Tol:
            if not iter % 1000:
                print(f'iter: {iter}, loss: {loss}')
            iter += 1
            self.thetas += (-1)*self.alpha*self.grads().T
            loss = self.loss()
            self.train.append(loss)
        print('Saving results')
        # Plotting
        fig, ax = plt.subplots(figsize=(10, 10))
        sns.lineplot(range(iter), self.train, ax=ax)
        fig.savefig(savefig)

    def plot_region(self, X):
        '''

        :param X:
        :return:
        '''
        # Get plot corners (add and substract 1 to include all points)
        (x1_min, x2_min) = X.min(axis=0) - 1
        (x1_max, x2_max) = X.max(axis=0) + 1
        # Generate axis
        x1_axis = np.arange(x1_min, x1_max, step=.1)
        x2_axis = np.arange(x2_min, x2_max, step=.1)
        # Mesh grid
        x1x_, x2x_ = np.meshgrid(x1_axis, x2_axis)
        # Shape grid as features
        x1x = x1x_.flatten().reshape(-1, 1)
        x2x = x2x_.flatten().reshape(-1, 1)
        # Add bias term (vector of ones) and transpose (set into 'column' shape)
        new_X = np.hstack((np.ones(x1x.shape), x1x, x2x)).T
        # Generate predictions and shape them as grid.
        y_hat = self.forward(new_X).reshape(x1x_.shape)
        # Generate plot
        fig, ax = plt.subplots(figsize=(10, 10))
        # Classification contour (notice that we need the grid shape)
        ax.contourf(x1x_, x2x_, y_hat)
        # Add population points
        sns.scatterplot(x='x1', y='x2', hue='class',
                        data=pd.DataFrame(np.hstack((self.y.T, X)),
                                          columns=['class', 'x1', 'x2']),
                        ax=ax)
        print('Saving classification region plot')
        fig.savefig('class_region.png')

    @staticmethod
    def normalize(X):
        '''
        x is a column vector of X
        :return: (x - mean(x))/sd(x)
        '''
        return (X - X.mean(axis=0, keepdims=True))/X.std(axis=0, keepdims=True)











