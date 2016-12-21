def function1(x,y,z):
    """
    no optional parameters here, instead we'll just pass everything explicitly, the sum of x,y,z
    
    params:
    @x - should be an int or float
    @y - should be an int or float
    @z - should be an int or float
    
    returns:
    An integer or float
    """
    return x + y + z

def function2(x,y,z=12):
    """
    optional parameters here, x,y are required, z is optional
    
    params:
    @x - should be an int or float
    @y - should be an int or float
    @z - should be an int or float
    
    returns:
    An integer or float
    """
    return x + y + z

def function3(**kwargs):
    return kwargs

def function4(*args):
    return args
    
if __name__ == '__main__':
    import code
    code.interact(local=locals())
