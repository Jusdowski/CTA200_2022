def z_iteration(c,num_iter):
    '''Iterates the equation z = z**2 + c for the given number of iterations, starting with z=0.
    
    Parameters
    ----------
    c : ndarray or complex number(float or int)
        2D array containing complex floats or a singular complex number
        
    num_iter: integer
              The maximum number of iterations.
        
    Returns
    -------
    z : ndarray or complex number(float or int)
        2D array containing the values of z = z**2 + c after iterating through 
        the maximum number of iterations for an array of c values or the complex number obtained
        after iterating through the maximum number of iterations for one value of c.
    '''
    
    z = 0
    
    for i in range (num_iter):
        z = z*z + c
        
    return z
