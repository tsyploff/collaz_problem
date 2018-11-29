#solution

def collaz_sequence_len(n):
    '''Вычисляет длину сиракузской последовательности

    >>> collaz_sequence_len(3)
    8
    >>> collaz_sequence_len(100)
    26
    
    '''
    m, s = n, 1
    while m != 1:
        if m%2 == 0:
            m, s = m//2, s+1
        else:
            m, s = 3*m+1, s+1
    return s

def longest_by_collaz_sequence(n):
    '''Ищет число с самой длинной сиракузской последовательностью

    >>> longest_by_collaz_sequence(1000)
    871
    >>> longest_by_collaz_sequence(10000)
    6171

    '''
    a = [collaz_sequence_len(i) for i in range(1, n+1)]
    return a.index(max(a)) + 1
    
import doctest
doctest.testmod()
