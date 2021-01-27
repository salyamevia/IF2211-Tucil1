# ------------- EXPERIMENTAL PURPOSES ONLY ------------- #

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
        lamb = [[]]
        l = len(x)
        groups = [list(digits)] * 3
        #print(groups)
        temp = []
        for i in groups:
            final = [x+[y] for x in final for y in i]
            print (final)
        for k in final:
            yield ''.join(k)

import time
start = time.time()
#list(products(digits))
#print(list(products(digits)))
#test = ''.join(tuple(str(int(digits[i])+1) for i in list(range(3))[:3] if digits[i] != 0 ))
#test = [x+[y] 

def permutation(length, lst): 
    if len(lst) == 0: return [] 
    if len(lst) == 1: return [lst] 
    if length == 1: return [x for x in range(10)] 
    l = [] 
    for i in range(len(lst)): 
       m = lst[i] 
       remLst = lst[:i] + lst[i+1:] 
       for p in permutation(length, remLst): 
           for i in range(length):
            l.append([m] + p) 
    return l 
  
# Driver program to test above function 
#data = list('123') 
#for p in permutation(2, data): 
#    print (p)

def initCryp(arr):
    # Find Unique
    temp = []; res = []
    for i in arr:
        if (not(i[0] in temp)): temp.append(i[0])
        for j in i:
           #if (not([j, 0] in res) and not(j.isspace())):
           if (not(j in res) and not(j.isspace())):
                res.append(j)
    
    arrFirst = []
    for i in temp:
        arrFirst.append(res.index(i))

    # Init Dict
    d = {'unique' : res, 'assign' : [0 for i in range(len(res))], 
            'firstPos' : arrFirst, 'combi' : [],
            'arr' : arr, 'time' : 0, 'iter' : 0}

    return d

def checker(dicti):
    arr = []
    
    for word in dicti['arr']:
        li = []
        for char in word:
            temp = dicti['assign'][dicti['unique'].index(char)]
            li.append(str(temp))
        arr.append(int(''.join(li)))
    
    #print(arr)
    #print(sum(arr[:len(arr)-1]) , "   " , arr[-1:][0])
    #print(sum(arr[:len(arr)-1]) == arr[-1:][0])

    if (sum(arr[:len(arr)-1]) == arr[-1:][0]):
        dicti['combi'].append(dicti['assign'])
        print(dicti['assign'])

def eugh_eight_loop(dicti):
    firstPos = dicti['firstPos']
    #l = []
    for a in range(10):
        if (0 in firstPos) and (a == 0):
            continue
        for b in range(10):
            if (1 in firstPos) and (b == 0):
               continue
            for c in range(10):
                if (2 in firstPos) and (c == 0): 
                    continue
                for d in range(10):
                    if (3 in firstPos) and (d == 0): 
                        continue
                    for e in range(10):
                        if (4 in firstPos) and (e == 0): 
                            continue
                        for f in range(10):
                            if (5 in firstPos) and (f == 0): 
                                continue
                            for g in range(10):
                                if (6 in firstPos) and (g == 0): 
                                    continue
                                for h in range(10):
                                    if (7 in firstPos) and (h == 0): 
                                        continue
                                    if (len([a,b,c,d,e,f,g,h]) == len(set([a,b,c,d,e,f,g,h]))):
                                        #l.append(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h))
                                        #print(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h))
                                        dicti['assign'] = [a,b,c,d,e,f,g,h]
                                        checker(dicti)
                                    else:
                                        continue
    #return l

#print(l)
init = initCryp(['SEND', 'MORE', 'MONEY'])
#eugh_eight_loop(init)
#init['assign'] = [9,5,6,7,1,0,8,2]
#checker(init)
init['time'] = time.time() - start
print(init)
t = ['SEND', 'MORE', 'HUH-HAH', 'MONEY']
s = ' + '.join(t[:len(t)-1])
s = s + ' = ' + t[len(t)-1]
print(s)

c = {'unique': ['A', 'B', 'C'],
            'combi': [[1,2,3], [4,5,6]]}

for i in range(len(c['unique'])):
    for j in range(len(c['combi'])):
        print(c['unique'][i],"=",c['combi'][j][i]," ",end="")
    print('')
