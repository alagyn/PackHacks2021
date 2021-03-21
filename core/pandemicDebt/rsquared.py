import numpy as np


def rSquared(a, b):
    # calculate R^2
    corrMatrix = np.corrcoef(a, b)
    corrXY = corrMatrix[0, 1]
    return corrXY ** 2
