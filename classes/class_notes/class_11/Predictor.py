import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class logit:

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


    def grads(self):
        '''
        dL/dbeta_j = (-1/n sum_i_n (yi-y_h_i)*xij)
        :return:
        '''
        y_hat = self.forward(self.X)

    def optimize(self, err=.01, Tol=1e5, savefig='error.png'):
        '''

        :return:
        '''
        iter = 0
        loss = self.loss()
        print('Training')
        while loss > err and iter < Tol:
            print(f'loss: {loss}')
            iter += 1
        print('Saving results')
        # Plotting
        fig, ax = plt.subplots(figsize=(10, 10))
        sns.lineplot(range(iter), self.train, ax=ax)
        fig.savefig(savefig)



    @staticmethod
    def normalize(X):
        '''

        :return:
        '''
       










