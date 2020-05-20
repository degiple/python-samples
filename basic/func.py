def double(x):
    """ Takes an int and returns it multiplied by 2.

    Args:
        x (int): 適当な数字

    Returns:
        int: x multiplied by 2.
    """
    return x**2


def str_print(s):
    """[summary]

    Args:
        s ([type]): [description]
    """
    print(s)


def arguments(a, b, c, d=3, e=4):
    """ Returns the result of two optional params multiplied by the addition of 3 required params.

    Args:
        a (int): [description]
        b (int): [description]
        c (int): [description]
        d (int, optional): [description]. Defaults to 3.
        e (int, optional): [description]. Defaults to 4.

    Returns:
        [type]: [description]
    """
    return a + b + c + (d * e)


def divide_by_2(x):
    """[summary]

    Args:
        x ([type]): [description]

    Returns:
        [type]: [description]
    """
    return x / 2


def multiply_by_4(x):
    """[summary]

    Args:
        x ([type]): [description]

    Returns:
        [type]: [description]
    """
    return x * 4


def convert(str):
    """[summary]

    Args:
        str ([type]): [description]

    Returns:
        [type]: [description]
    """
    try:
        return float(str)
    except ValueError:
        print("Could not convert the string to a float.")


print(convert("111"))
