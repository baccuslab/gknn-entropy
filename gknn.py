"""
Generalized k-nearest neighbor entropy estimation
authors: Niru Maheswaranathan and Lane McIntosh
04:16 PM Apr 7, 2014
"""

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
    pass

def volume(radii, ball):
    """
    Computes the volume of the given ball with given radius

    input
    -----
    radii (nd-array):
        A set of radius values to use when computing volume

    ball (string):
        Which ball (e.g. l1, euclidean, etc.) to use when computing the volume

    output
    ------
    volume (nd-array):
        A set of computed volumes, one for each given radius

    """
    pass

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
        0: Chebyshev (l_inf) ball
        1: Manhattan (l1) ball
        2: Euclidean (l2) ball

    """

    # Euclidean ball
    if string.upper() == 'L2' or string.upper() == 'EUCLIDEAN':
        return 2

    # l1 ball
    elif string.upper() == 'L1' or string.upper() == 'MANHATTAN' or string.upper() == 'TAXICAB':
        return 1

    elif string.upper() == 'LINF' or string.upper() == 'CHEBYSHEV':
        return 0

    # ball not found
    else:
        raise ValueError('Could not recognize the ' + string + ' ball.')

if __name__=="__main__":
    pass
