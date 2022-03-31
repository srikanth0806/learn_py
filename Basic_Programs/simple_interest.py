def simple_interest( p, t, r ):
    """
    :param p: principal amount
    :param t: time
    :param r: rate
    :return: simple interest
    """
    si = p*t*r/100
    return si
print(simple_interest(1000,2,5))
print(help(simple_interest))
