def z_iteration(c,num_iter):
    '''Iterates the equation z = z**2 + c for the given number of iterations, starting with z=0.
    
    Parameters
    ----------
    c : ndarray
        2D array containing complex floats.
        
    num_iter: integer
              The maximum number of iterations.
        
    Returns
    -------
    z : ndarray
        2D array containing the absolute values of z = z**2 + c after iterating through 
        the maximum number of iterations.
    '''
    
    z = 0
    
    for i in range (num_iter):
        z = z*z + c
        
    return z
