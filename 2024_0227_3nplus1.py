def three_n_plus(n):
    
    """
    Entra un nùmero n
    
    Sale el número de pasos en que se tarda en llegar a 1
    
    >>> three_n_plus(6)
        8
    >>> three_n_plus(3)
        7
        
    """
    p=0
    while n!=1:
        p = p+1
        
        if n%2==0:
            n = n/2
        else:
            n = (3*n)+1
        
    
    print(p)
