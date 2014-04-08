"""
Generalized k-nearest neighbor entropy estimation
authors: Niru Maheswaranathan and Lane McIntosh
04:16 PM Apr 7, 2014
"""
import numpy as np
from math import gamma
from sklearn.neighbors import DistanceMetric

def entropy(data, ball='euclidean', k=1, units='nats'):
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

    units (string):
        Which unit the entropy output has.
        Acceptable strings include:
            'nats' : base e
            'bits' : base 2

    """
    
    # Get number of samples and dimensionality
    (n,p)  = data.shape
    
    # Determine radii and volumes for a given metric space
    metric = getball(ball)
    if metric == 1:
        m = 'manhattan'
    elif metric == 2:
        m = 'euclidean'
    elif metric == inf:
        m = 'chebyshev'
        
    dist  = DistanceMetric.get_metric(m)
    D_mat = dist.pairwise(data)
    D_mat.sort(axis=1)
    radii = D_mat[:,k]
    Vs    = volume(radii, ball=str(metric), dimension=p)
    
    if units.lower() == 'nats':
        return sum([np.log(vol) for vol in Vs])/float(n) + np.log(n) - L(k - 1) + 0.577215665
    if units.lower() == 'bits':
        return sum([np.log2(vol) for vol in Vs])/float(n) + np.log2(n) - L(k - 1) + 0.577215665

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
    if string.upper() == 'L2' or string.upper() == 'EUCLIDEAN' or string == '2':
        return 2

    # l1 ball
    elif string.upper() == 'L1' or string.upper() == 'MANHATTAN' or string.upper() == 'TAXICAB' or string == '1':
        return 1

    elif string.upper() == 'LINF' or string.upper() == 'CHEBYSHEV' or string == 'inf':
        return float('inf')

    # ball not found
    else:
        raise ValueError('Could not recognize the ' + string + ' ball.')

def L(k):
    if k == 0:
        return 0
    elif k > 0:
        return sum([1/float(i) for i in xrange(1,k+1)])



if __name__=="__main__":
    pass
