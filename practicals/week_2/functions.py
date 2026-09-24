def cookies_needed(adults: int, teens: int, children: int) -> int:
    '''Return the number of cookies needed to
    feed this number of adults, teens and children.
    Each adult eats two, each teen six, and each child three.
    >>> cookies_needed(2, 3, 1)
    25
    '''
    adults_cookies = 2
    teen_cookies = 6
    child_cookies = 3
    return adults_cookies * adults + teen_cookies * teens + child_cookies * children

def is_multiple_of_7(x: int) -> bool:
    '''Return True iff 7 divides x without a remainder.
    >>> is_multiple_of_7(15)
    False
    >>> is_multiple_of_7(7)
    True
    '''
    return is_multiple(x,7)

def is_multiple(x: int, y: int) -> bool:
    '''Return True iff y divides x without a remainder.
    >>> is_multiple(15, 3)
    True
    >>> is_multiple(7, 2)
    False
    '''
    return x % y == 0