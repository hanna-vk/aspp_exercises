"""
A collection of simple math operations:
- simple_add for addition of two numbers a and b
- simple_sub for subtraction of two numbers a and b
- simple_mult for multiplication of two numbers a and b
- simple_div for division of two numbers a and b
- poly_first for a first degree polynomial
- poly_second for a second degree polynomial
"""

def simple_add(a,b):
    """
    Calculating the sum of two numbers a and b.
    Parameters
    ----------
    a : integer
    First number to be added.
    -------
    b : integer
    Second number to be added.
    Examples
    --------
    >>> simple_math.simple_add(1,1)
    2
    >>> simple_math.simple_add(3,2) 
    5
    """
    return a+b

def simple_sub(a,b):
    """
    Subtracting number b from number a.
    Parameters
    ----------
    a : integer
    First number to be added.
    -------
    b : integer
    Second number to be subtracted.
    Examples
    --------
    >>> simple_math.simple_sub(1,1)
    0
    >>> simple_math.simple_sub(3,2) 
    1
    """    
    return a-b

def simple_mult(a,b):
    """
    Multiplying a with b.
    Parameters
    ----------
    a : integer
    First number.
    -------
    b : integer
    Second number.
    Examples
    --------
    >>> simple_math.simple_mult(1,1)
    1
    >>> simple_math.simple_mult(3,2) 
    6
    """
    return a*b

def simple_div(a,b):
    """
    Dividing a by b.
    Parameters
    ----------
    a : integer
    First number.
    -------
    b : integer
    Second number.
    Examples
    --------
    >>> simple_math.simple_div(1,1)
    1
    >>> simple_math.simple_div(3,2) 
    1.5
    """
    return a/b

def poly_first(x, a0, a1):
    """
    Evaluating a first degree polynomial y = a0 + a1*x.
    Parameters
    ----------
    a0 : integer
    Intercept.
    -------
    a1 : integer
    Gain.
    -------
    x : integer
    Point of evaluation. 
    Examples
    --------
    >>> simple_math.poly_first(1,1,1)
    2
    >>> simple_math.poly_first(3,2,1) 
    5
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """
    Evaluating a second degree polynomial y = a0 + a1*x + a2*(x^2).
    Parameters
    ----------
    a0 : integer
    Intercept.
    -------
    a1 : integer
    Parameter for first degree x.
    -------
    a1 : integer
    Parameter for second degree x^2.
    -------
    x : integer
    Point of evaluation. 
    Examples
    --------
    >>> simple_math.poly_first(1,1,1)
    2
    >>> simple_math.poly_first(3,2,1) 
    5
    """
    return poly_first(x, a0, a1) + a2*(x**2)
