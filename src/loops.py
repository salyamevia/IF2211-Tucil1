
#-------------- CHECKER --------------#
def checker(dicti):
    arr = []
    
    for word in dicti['arr']:
        li = []
        for char in word:
            temp = dicti['assign'][dicti['unique'].index(char)]
            li.append(str(temp))
        arr.append(int(''.join(li)))

    if (sum(arr[:len(arr)-1]) == arr[-1:][0]):
        dicti['combi'].append(dicti['assign'])
        #print(dicti['assign'])

#-------------- LOOPS --------------#
#-------------- ONE --------------#
def one_loop(dicti):
    firstPos = dicti['firstPos']; iter = 0
    for a in range(10):
        if (0 in firstPos) and (a == 0):
            continue
        if (len([a]) == len(set([a]))):
            dicti['assign'] = [a]; iter+=1
            checker(dicti)
        else:
            continue
    dicti['iter'] = iter

#-------------- TWO --------------#
def two_loop(dicti):
    firstPos = dicti['firstPos']; iter = 0
    for a in range(10):
        if (0 in firstPos) and (a == 0):
            continue
        for b in range(10):
            if (1 in firstPos) and (b == 0):
               continue
            if (len([a,b]) == len(set([a,b]))):
                dicti['assign'] = [a,b]; iter+=1
                checker(dicti)
            else:
                continue
    dicti['iter'] = iter

#-------------- THREE --------------#
def three_loop(dicti):
    firstPos = dicti['firstPos']; iter = 0
    for a in range(10):
        if (0 in firstPos) and (a == 0):
            continue
        for b in range(10):
            if (1 in firstPos) and (b == 0):
               continue
            for c in range(10):
                if (2 in firstPos) and (c == 0): 
                    continue
                if (len([a,b,c]) == len(set([a,b,c]))):
                    dicti['assign'] = [a,b,c]; iter+=1
                    checker(dicti)
                else:
                    continue
    dicti['iter'] = iter

#-------------- FOUR --------------#
def four_loop(dicti):
    firstPos = dicti['firstPos']; iter = 0
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
                    if (len([a,b,c,d]) == len(set([a,b,c,d]))):
                        dicti['assign'] = [a,b,c,d]; iter+=1
                        checker(dicti)
                    else:
                        continue
    dicti['iter'] = iter

#-------------- FIVE --------------#
def five_loop(dicti):
    firstPos = dicti['firstPos']; iter = 0
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
                        if (len([a,b,c,d,e]) == len(set([a,b,c,d,e]))):
                            dicti['assign'] = [a,b,c,d,e]; iter+=1
                            checker(dicti)
                        else:
                            continue
    dicti['iter'] = iter

#-------------- SIX --------------#
def six_loop(dicti):
    firstPos = dicti['firstPos']; iter = 0
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
                            if (len([a,b,c,d,e,f]) == len(set([a,b,c,d,e,f]))):
                                dicti['assign'] = [a,b,c,d,e,f]; iter+=1
                                checker(dicti)
                            else:
                                continue
    dicti['iter'] = iter

#-------------- SEVEN --------------#
def seven_loop(dicti):
    firstPos = dicti['firstPos']; iter = 0
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
                                if (len([a,b,c,d,e,f,g]) == len(set([a,b,c,d,e,f,g]))):
                                    dicti['assign'] = [a,b,c,d,e,f,g]; iter+=1
                                    checker(dicti)
                                else:
                                    continue
    dicti['iter'] = iter

#-------------- EIGHT --------------#
def eight_loop(dicti):
    firstPos = dicti['firstPos']; iter = 0
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
                                        dicti['assign'] = [a,b,c,d,e,f,g,h]; iter+=1
                                        checker(dicti)
                                    else:
                                        continue
    dicti['iter'] = iter

#-------------- NINE --------------#
def nine_loop(dicti):
    firstPos = dicti['firstPos']; iter = 0
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
                                    for i in range(10):
                                        if (8 in firstPos) and (i == 0): 
                                            continue
                                        if (len([a,b,c,d,e,f,g,h,i]) == len(set([a,b,c,d,e,f,g,h,i]))):
                                            dicti['assign'] = [a,b,c,d,e,f,g,h,i]; iter+=1
                                            checker(dicti)
                                        else:
                                            continue
    dicti['iter'] = iter

#-------------- TEN --------------#
def ten_loop(dicti):
    firstPos = dicti['firstPos']; iter = 0
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
                                    for i in range(10):
                                        if (8 in firstPos) and (i == 0): 
                                            continue
                                        for j in range(10):
                                            if (9 in firstPos) and (j == 0): 
                                                continue
                                            if (len([a,b,c,d,e,f,g,h,i,j]) == len(set([a,b,c,d,e,f,g,h,i,j]))):
                                                dicti['assign'] = [a,b,c,d,e,f,g,h,i,j]; iter+=1
                                                checker(dicti)
                                            else:
                                                continue
    dicti['iter'] = iter