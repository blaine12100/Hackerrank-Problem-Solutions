def gcd(a, b):

    """The GCD or the Greatest Common Divisor is the highest possilbe number which is
    able to divide the 2 Numbers.Here the Naive Approach will be to factorize both the numbers and
    then take an intersection of their factors and get the max common factor.The problem with this
    approach is that if the numbers become too long,then the numbers will not fit
    
    So we use the Euclid's GCD algorithm approach which states that the GCD of 2 numbers A
    and B is the same as the the GCB of B and the remainder of A%B"""

    # Our loop/recursive guard condition
    if b == 0:
        return a

    else:
        return gcd(b, a % b)
