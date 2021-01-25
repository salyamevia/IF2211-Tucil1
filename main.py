import time
import random
import math

# Read File
filename = input("Enter filename (.txt only): ")

f = open(filename+".txt", "r")

# Assign to Array
i = 0; j = 0; strAll = []; strTemp = []
for x in f:
    if (x == '\n'):
        #print("huh-hah"); print(strTemp);
        x = f.readline()
        strAll.append(strTemp); strTemp = []
    
    if (x[0] == '-'):
        x = f.readline()
        x = x.strip()
        strTemp.append(x)
    else:
        x = x.strip().strip('+')
        strTemp.append(x)

    #print(x, end=" ");
strAll.append(strTemp)
#print(strAll);

# Timer On
start = time.time()

# Asign to Unique Array
def initCryp(arr):
    # Find Unique
    arrFirst = []; res = []
    for i in arr:
        if (not(i[0] in arrFirst)): arrFirst.append(i[0])
        for j in i:
            if (not([j, 0] in res) and not(j.isspace())):
                res.append([j, 0])
    
    # Init Dict
    d = {'assign' : res, 'firstPos' : arrFirst, 'permutate' : [], 'combi' : [],
            'arr' : arr, 'time' : 0, 'iter' : 0}

    return d
    
dictAll = []
d = initCryp(strAll[0])
#a = initCryp(strAll[1])
dictAll.append(d) #dictAll.append(a);
print(dictAll)

# Checker
def checker(dicti):
    arr = []
    for word in dicti['arr']:
        li = []
        for char in word:
            temp = [str(k[1]) for k in dicti['assign'] if k[0] == char]
            li.append(temp[0])
        arr.append(int(''.join(li)))

    #print(arr)
    #print(sum(arr[:len(arr)-1]) , "   " , arr[-1:][0])
    #print(sum(arr[:len(arr)-1]) == arr[-1:][0])

    if (sum(arr[:len(arr)-1]) == arr[-1:][0]):
        dicti['combi'].append(dicti['assign'])


# Shuffle + Timer + Iteration check
def shuffler(dicti):
    # Random Assign + Check firstPost
    for i in dicti['assign']:
        if (i[0] in dicti['firstPos']): 
            i[1] = random.randint(1,9)
        else:
            i[1] = random.randint(0,9)

        #print(dicti['assign'])
        check = [True if ((j != i) and (j[1] == i[1])) else False for j in dicti['assign']]
        #print(check)

        while (True in check):
            if (i[0] in dicti['firstPos']): 
                i[1] = random.randint(1,9)
            else:
                i[1] = random.randint(0,9)
            check = [True if ((j != i) and (j[1] == i[1])) else False for j in dicti['assign']]

    #print(dicti['assign'])

# Permutate
def permutate(dicti):
    dicti['iter'] = math.factorial(len(d['assign']))
    for i in range(dicti['iter']):   
        shuffler(d)
        dicti['permutate'].append(dicti['assign'])
        checker(dicti)
    
    dicti['permutate'] = set(dicti['permutate'])

permutate(d)
# Timer Off
d['time'] = time.time() - start

print(d)

# TO DO LIST :
# COMBINATIONS BELUM KELUAR TOLOOONGGG WHAT IS WRONG
# PROBABLY TRY NOT SO RANDOM APPROACH AAAAA