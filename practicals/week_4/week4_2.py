def shorter(s1:str, s2: str) -> str:
    '''
    Return the shortest string.

    shorter("ab","abab")
    >>> ab

    shorter("abcd","ab")
    >>> ab
    '''
    if(s1 <= s2):
        return s1
    else :
        return s2

print(shorter("ab","abab"))
print(shorter("abcd","ab"))

def later(s1:str, s2: str) -> str:
    '''
    Return the string that appears later in the dictionary.

    later("CSC", "MAT")
    >>> "MAT"

    later("PHY", "MAT")
    >>> "PHY"
    '''
    if(s1 <= s2):
        return s2
    else:
        return s1
    
print(later("CSC", "MAT"))
print(later("PHY", "MAT"))

def without_letters(s: str, char: str) -> str | None:
    '''
    Return the length of the strin s, if it does not contain char.

    without_letters("MAT102", 'M')
    >>> None

    without_letters("MAT102", 'C')
    >>> 6
    '''
    if(char not in s):
        return len(s)
    else:
        return None

print(without_letters("MAT102", 'M'))
print(without_letters("MAT102", 'C'))

def remove_character(s:str, char:str) -> str:
    '''
    Return the original string without char in it.
    
    remove_character("MAT102", 'M'):
    >>> "AT102

    remove_character("MAT102", 'C'):
    >>> "MAT102"
    '''
    new_string=''
    for i in s:
        if (i != char):
            new_string +=i
        else:
            new_string
    return new_string

print(remove_character("MAT102", 'M'))
print(remove_character("MAT102", 'C'))

def where(s:str, ch:str)->int:
    '''
    Return the index of the last occurance of the charcter "ch" in s
    
    where("NOON", "N")
    >>> 3

    where("NOON", "O")
    >>> 2
    '''
    for i in range(len(s)-1,0,-1) :
        if(s[i]==ch):
            return i

print(where("NOON", "N"))
print(where("NOON", "O"))
        