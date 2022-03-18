import numpy as np

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


    def __init__(self, X, y):
        self.X = np.vstack((np.ones(y.shape), X.T))
        self.y = y.reshape(1, -1)
        self.thetas = np.random.rand(self.X.shape[0]).reshape(1, -1)

    def forward(self):
        '''
        Apply phi
        HINT 1: np.dot
        HINT 2: np.exp
        HINT 3: check the shape of theta!
        :return: phi(z)
        '''
        return 1/(1 + np.exp(np.dot(self.thetas, self.X)))

