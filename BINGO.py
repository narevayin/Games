import random
B = [1, 3, 7, 13, 15]
I = [17, 20, 22, 25, 28]
N = [31, 33, 38, 40, 44]
G = [47, 48, 50, 51, 56]
O = [61, 63, 68, 71, 74]

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28, 29, 30, 31, 32, 33, 34, 35, 36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75]

win = False

while win == False:
    n = random.choice(numbers)
    numbers.remove(n)
    print (n)


    if n in B:
        index = B.index(n)
        B[index] = 'x'
        print ('you have number',n)
        if B == ['x','x','x','x','x']:
            win = True
            print('you won')
    elif n in I:
        index = I.index(n)
        I[index] = 'x'
        print('you have number',n)
        if I == ['x','x','x','x','x']:
            win = True
            print('you won')
    elif n in N:
        index = N.index(n)
        N[index] = 'x'
        print('you have number',n)
        if N == ['x','x','x','x','x']:
            win = True
            print('you won')
    elif n in G:
        index = G.index(n)
        G[index] = 'x'
        print('you have number',n)
        if G == ['x','x','x','x','x']:
            win = True
            print('you won')
    elif n in O:
        index = O.index(n)
        O[index] = 'x'
        print('you have number',n)
        if O == ['x','x','x','x','x']:
            win = True
            print('you won')        
    elif B[0] == 'x' and I[0] == 'x' and N[0] == 'x'  and G[0] == 'x' and O[0] == 'x':
        win = True
        print('you won')
    elif B[1] == 'x' and I[1] == 'x' and N[1] == 'x'  and G[1] == 'x' and O[1] == 'x':
        win = True
        print('you won')
    elif B[2] == 'x' and I[2] == 'x' and N[2] == 'x'  and G[2] == 'x' and O[2] == 'x':
        win = True
        print('you won')
    elif B[3] == 'x' and I[3] == 'x' and N[3] == 'x'  and G[3] == 'x' and O[3] == 'x':
        n = True
        print('you won')
    elif B[4] == 'x' and I[4] == 'x' and N[4] == 'x'  and G[4] == 'x' and O[4] == 'x':
        n = True
        print('you won')
    elif B[0] == 'x' and I[1] == 'x' and N[2] == 'x'  and G[3] == 'x' and O[4] == 'x':
        n = True
        print('you won')
    elif B[4] == 'x' and I[3] == 'x' and N[2] == 'x'  and G[1] == 'x' and O[0] == 'x':
        n = True
        print('you won')
    print ('\n', B,'\n',I,'\n',N,'\n',G,'\n',O)


