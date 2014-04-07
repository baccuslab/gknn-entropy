"""
Generalized k-nearest neighbor entropy estimation
authors: Niru Maheswaranathan and Lane McIntosh
04:16 PM Apr 7, 2014
"""

def estentropy(data, ball, k):
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

if __name__=="__main__":
    pass
