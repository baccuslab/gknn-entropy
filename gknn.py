"""
Generalized k-nearest neighbor entropy estimation
authors: Niru Maheswaranathan and Lane McIntosh
04:16 PM Apr 7, 2014
"""
import numpy as np
from math import gamma

def entropy(data, ball, k):
    """
    Estimates the entropy of the given data using the k-nearest neighbors method

    input
    -----
    data (nd-array):
        An (n by p) matrix containing n samples of p-dimensional data

    ball (string):
        Which ball (e.g. l1, euclidean, etc.) to use when computing the volume.
        Acceptable strings include:
            'l1'   : l1 or Manhattan distance
            'l2'   : l2 or Euclidean distance; default
            'linf' : l-infinity or Chebyshev distance

    k (integer):
        How many nearest-neighbors to use when computing radii. Must be at least 1.

    """
    
    (n,p) = data.shape
    b     = getball(ball)
    V     = volume(radius,ball=b)
    
    
    H = sum([log(vol_i) for vol_i in V])/float(n) + log(n) - L(k - 1) + 0.577215665
    
    pass

def volume(radii, ball, dimension):
    """
    Computes the volume of the given ball with given radius

    input
    -----
    radii (nd-array):
        A set of radius values to use when computing volume

    ball (string):
        Which ball (e.g. l1, euclidean, etc.) to use when computing the volume

    dimension (integer):
        Dimensionality of the space in which to compute the volume

    output
    ------
    volume (nd-array):
        A set of computed volumes, one for each given radius

    """
    p = float(dimension)
    b = getball(ball)
    return (2*gamma(1/b + 1)*radii)**p / gamma(p/b + 1)

def getball(string):
    """
    Get index associated with a corresponding 'ball'

    input
    -----
    string:
        A given name of a 'ball' (e.g. euclidean, l1, l2, etc.)

    output
    ------
    index:
        An index (integer) associated with that ball:
        1: Manhattan (l1) ball
        2: Euclidean (l2) ball
        inf: Chebyshev (l_inf) ball

    """

    # Euclidean ball
    if string.upper() == 'L2' or string.upper() == 'EUCLIDEAN':
        return 2

    # l1 ball
    elif string.upper() == 'L1' or string.upper() == 'MANHATTAN' or string.upper() == 'TAXICAB':
        return 1

    elif string.upper() == 'LINF' or string.upper() == 'CHEBYSHEV':
        return float('inf')

    # ball not found
    else:
        raise ValueError('Could not recognize the ' + string + ' ball.')

if __name__=="__main__":
    pass
