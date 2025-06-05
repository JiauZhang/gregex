ZERO_OR_MORE = r'*'
ONE_OR_MORE = r'+'
ZERO_OR_ONE = r'?'
LAZY_ZERO_OR_MORE = r'*?'
LAZY_ONE_OR_MORE = r'+?'
LAZY_ZERO_OR_ONE = r'??'

def exactly(n):
    return r'{' + str(n) + r'}'

def least(n, lazy=False):
    pattern = r'{' + str(n) + r',}'
    if lazy: pattern += r'?'
    return pattern

def range(n, m, lazy=False):
    pattern = r'{' + f'{n},{m}' + r'}'
    if lazy: pattern += r'?'
    return pattern
