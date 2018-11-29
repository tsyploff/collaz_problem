#best_solution

cashe_collaz = dict()

def collaz_sequence_len(n):
    '''Вычисляет длину сиракузской последовательности

    >>> collaz_sequence_len(3)
    8
    >>> collaz_sequence_len(100)
    26
    
    '''
    global cashe_collaz
    if n == 1:
        return 1
    elif n in cashe_collaz:
        return cashe_collaz[n]
    else:
        if n%2 == 0:
            s = 1 + collaz_sequence_len(n//2)
            cashe_collaz[n] = s
            return s
        else:
            s = 1 + collaz_sequence_len(3*n+1)
            cashe_collaz[n] = s
            return s

def longest_by_collaz_sequence(n):
    '''Ищет число с самой длинной сиракузской последовательностью

    >>> longest_by_collaz_sequence(1000)
    871
    >>> longest_by_collaz_sequence(10000)
    6171

    '''
    a, b = 1, 1
    for i in range(1, n+1):
        j = collaz_sequence_len(i)
        if j > b:
            a, b = i, j
        else:
            continue
    return a

import doctest
doctest.testmod()
