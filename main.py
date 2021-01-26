import time

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
           if (not(j in res) and not(j.isspace())):
                res.append(j)
    
    # Init Dict
    d = {'unique' : res, 'assign' : [0 for i in range(len(res))], 
            'firstPos' : arrFirst, 'combi' : [],
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
            temp = dicti['assign'][dicti['unique'].index(char)]
            li.append(str(temp))
        arr.append(int(''.join(li)))
    
    #print(arr)
    #print(sum(arr[:len(arr)-1]) , "   " , arr[-1:][0])
    #print(sum(arr[:len(arr)-1]) == arr[-1:][0])

    if (sum(arr[:len(arr)-1]) == arr[-1:][0]):
        dicti['combi'].append(dicti['assign'])



# Permutate
def permutate(dicti):
    def rand(dicti, range, length):
        possibility = list(map(tuple, range)) * length
        res = [[]]
        for pos in possibility:
            res = [x+[y] for x in res for y in pos]
       
        dicti['iter'] = len(res)
        for prod in res:
            yield tuple(prod)

    
    digits = ('1','2','3','4','5','6','7','8','9')
    for x in rand(dicti, range(10), len(dicti['unique'])):
        if len(set(x)) == len(dicti['unique']):
            yield tuple(digits[i] for i in x)
    
    


#permutate(d)
# Timer Off
d['time'] = time.time() - start


print(d)

# TO DO LIST :
# COMBINATIONS BELUM KELUAR TOLOOONGGG WHAT IS WRONG
# PROBABLY TRY NOT SO RANDOM APPROACH AAAAA