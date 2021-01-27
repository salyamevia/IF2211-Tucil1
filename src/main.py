import time
import loops # File fungsi iterasi

print("===== CRYPTARITHMETIC SOLVER =====")
print("This program is using a brute force algorithm, so it may take some time depending on your computer power.")
print("You can add more than 1 (one) problem each file. Use `./folder_name/file_name` if it's on another directory.")
print("")

#-------------- INPUT PROBLEMS --------------#
# Read File
filename = input("Enter filename (.txt only): ")
f = open(filename+".txt", "r")

# Assign to Array
i = 0; j = 0; strAll = []; strTemp = []
for x in f:
    if (x == '\n'):
        x = f.readline()
        strAll.append(strTemp); strTemp = []
    
    if (x[0] == '-'):
        x = f.readline()
        x = x.strip()
        strTemp.append(x)
    else:
        x = x.strip().strip('+')
        strTemp.append(x)
strAll.append(strTemp)

#-------------- ASSIGN --------------#
# Asign to Unique Array
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

#-------------- SOLVER --------------#
# Permutate
for problem in strAll:
    start = time.time()
    print('--- Solving Problem ---')
    s = ' + '.join(problem[:len(problem)-1])
    s = s + ' = ' + problem[len(problem)-1]
    print("Problem: ", s)

    d = initCryp(problem)
    length = len(d['unique'])
    if (length == 1):
        loops.one_loop(d)
    elif (length == 2):
        loops.two_loop(d)
    elif (length == 3):
        loops.three_loop(d)
    elif (length == 4):
        loops.four_loop(d)
    elif (length == 5):
        loops.five_loop(d)
    elif (length == 6):
        loops.six_loop(d)
    elif (length == 7):
        loops.seven_loop(d)
    elif (length == 8):
        loops.eight_loop(d)
    elif (length == 9):
        loops.nine_loop(d)
    elif (length == 10):
        loops.ten_loop(d)
    else:
        print("Error.")

    # Results
    print("")
    print('--- Results ---')
    print(len(d['combi'])," solution(s) found." )
    for i in range(len(d['unique'])):
        for j in range(len(d['combi'])):
            print(d['unique'][i],"=",d['combi'][j][i]," ",end="")
        print('')

    print("Iterations: ", d['iter'])
    
    d['time'] = time.time() - start
    print("Time taken: ", d['time'])
    print("")
    #print(d)

#-------------- DELAY --------------#
input('Press ENTER to exit. To try again, you need to close and reopen the program.')