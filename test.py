from itertools import chain, permutations
from string import digits

def solve_cryptarithm(addends, result):
    """Print a solution to the cryptarithm, if any exists.
    Arguments are the list of addends and the result of the sum.
    For example:

    >>> solve_cryptarithm(['SEND', 'MORE'], 'MONEY')
    SEND(9567) + MORE(1085) = MONEY(10652)

    """
    letters = ''.join(set(chain(result, *addends)))
    print(letters)
    initial_letters = ''.join(set(chain(result[0], (a[0] for a in addends))))
    print(initial_letters)
    for perm in permutations(digits, len(letters)):
        decipher_table = str.maketrans(letters, ''.join(perm))
        def decipher(s):
            return s.translate(decipher_table)
        if '0' in decipher(initial_letters):
            continue # leading zeros not allowed
        deciphered_sum = sum(int(decipher(addend)) for addend in addends)
        if deciphered_sum == int(decipher(result)):
            def fmt(s):
                return f"{s}({decipher(s)})"
            print(" + ".join(map(fmt, addends)), "=", fmt(result))
            break
    else:
        print(" + ".join(addends), "=", result, " : no solution")

#solve_cryptarithm(['SEND', 'MORE'], 'MONEY')

def product(args, kwds):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    #print(kwds.get('repeat', 1))
    print(kwds)
    pools = tuple(args) * kwds
    print(pools)
    result = [[]]
    for pool in pools:
        print(pool)
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

#print(list(product(range(10), 3)))
#print(tuple(range(10)))
#print(tuple(digits))

def product(*args, **kwds):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    #pools = map(tuple, args) * kwds.get('repeat', 1)
    pools = [list(args)] * kwds
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

def products(x):
        final = [[]]
        l = len(x)
        groups = [list(x)] * l
        print(groups)
        for i in groups:
            final = [x+[y] for x in final for y in i]
        for k in final:
            yield ''.join(k)

print(list(products(digits)))