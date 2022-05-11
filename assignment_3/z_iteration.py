def z_iteration(c, num_iter):
    '''Iterates the equation zi+1 = zi**2 + c for the given number of iterations, starting with z0=0.
    
    Parameters
    ----------
    c : complex number(float or int)
        The complex coordinate value that will be used in the iteration.
        
    num_iter: integer
              The maximum number of iterations. 
        
    Returns
    -------
    zi : array 
         1D array containing the values of z = z**2 + c after iterating through 
         the maximum number of iterations for the given value of c .
         
    n: array
       1D array containing the number of iterations for which point c diverges which is determined to be when abs(zi) > 2. 
       '''
    z0 = 0
    i = 0
    
    zi = []
    n = [] 
    
    while i <= num_iter: 
        
        if i == 0:
            z1 = z0*z0 + c 
            zi.append(z1)
            
        if i > 0:
            z = zi[i-1]**2 + c 
            zi.append(z)
        
        if abs(zi[i]) > 2: 
            n.append(i)
            break
            
        i = i + 1
        
    return zi, n
        
        
    return z, zi, n 
