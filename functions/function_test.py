def max_of_two(a, b):
    """
    max_of_two function will take two  arguments.
    and return big one among them
    :param a: it is position argument must be integer or float
    :param b: it is a positional argumment must be inter or float
    :return: return big among a and b
    """
    if a > b:
        return a
        print("a is big")
    else:
        return b
        print("b is big")
max_of_two(15,18)
print(help(max_of_two))